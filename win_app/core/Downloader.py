import paramiko
import subprocess
import sys
import time
import logging

from core.ProcessMonitor import ProcessMonitor
from objects.Database import Database
from objects.Device import Device
from common import constants
from common.Singleton import Singleton
import objects.connections
from objects.connections import TCPConnection

MONITORED_PROCESS = 'ShExe.exe'

class Downloader(metaclass=Singleton):

    def download_build(target_device: Device,
                       target_connection: TCPConnection,
                       target_database: Database) -> None:
        
        __target_connection = target_connection

        __monitored_process = MONITORED_PROCESS

        try: 
            logging.info(f'Attempting download with database "{target_database.get_filename()}" via "{__target_connection.get_type().upper()}" "{__target_connection.get_id()}", to "{target_device.get_device_id()}"')

            match type(__target_connection):
                case objects.connections.TCPConnection:
                    command_args = [str(constants.CRIMSON_INSTALL),
                                    '-send',
                                    '-TCP',
                                    __target_connection.get_remote_host_address(),
                                    str(target_database.get_filepath()),
                                    '-user',
                                    constants.CRIMSON_USER,
                                    '-pass',
                                    constants.CRIMSON_PASS]
                    
                    Downloader.__run_c3(command_args, __monitored_process)
        
        except Exception as e:
            logging.error(f'Unexpected Exception encountered while attempting download of "{target_database.get_id()}" build via {__target_connection.get_type()} to device "{target_device.get_id()}", "{e}"')
            logging.error('Please verify that all config files are correct and that all physical connections to device are stable and try again')
            logging.info('Beginning cleanup...')
            sys.exit()

    def __run_c3(command_args: list, monitored_process: str) -> None:
        try:
            __initial_instance_pids = ProcessMonitor.find_all_process_instances(monitored_process, is_initial_search=True)
            subprocess.Popen(command_args)
            # init search for "monitored process" PID, which is used to monitor the lifespan of the Crimson download on the target device
            __target_instance_pid = ProcessMonitor.find_target_instance_pid(monitored_process, __initial_instance_pids)
            ProcessMonitor.check_for_download_completion(__target_instance_pid)
        
        finally:
            # attempt to terminate target "ShExe.exe" process, in case of hanging process
            try:
                logging.info(f'Terminating target process, PID {__target_instance_pid}')
                subprocess.run(["C:\\Windows\\system32\\taskkill.exe",
                                '/F',
                                '/PID',
                                str(__target_instance_pid)])
            
            # if download process was aborted, the above subprocess.run will hit an exception
            except Exception as e:
                logging.info(f'Error encountered while attempting to terminate the target process, {e}')
                pass

    def __check_ssh(device: Device) -> bool:
        '''
        This method checks if the target device is open to SSH communication by attempting to establish an SSH connection.
        
        **Parameters**:  
        - *device* -- `Device`
            - The target device to check for SSH communication.
        ---
        **Returns**:
        - **bool**: `True` if the device is open to SSH communication, `False` otherwise.
        '''
        __remote_host = device.get_tcp_connection().get_remote_host_address()
        __ssh_user = device.get_os_settings().get_ssh_user()
        __password = device.get_os_settings().get_ssh_password()
        
        logging.info(f'Polling device "{device.get_id()}" for open comms...')
        try:
            # Create an SSH client
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the host
            ssh.connect(__remote_host, username=__ssh_user, password=__password)
            logging.info(f'SSH connection to {__remote_host} successfully established')

            # Close the connection
            ssh.close()
            logging.info(f'SSH connection to {__remote_host} successfully closed')
        
        except Exception as e:
            logging.error('Device still closed to communication -- trying again...')
            return False
            
        return True