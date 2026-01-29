import ipaddress
import re
import subprocess
import sys
import logging 

from common.connection import Connection
from core.socketHandler import SocketHandler
from common import constants

class TCPConnection(Connection):

    # connection will always be ethernet unless USB is implemented in which a USB class will need to be added, and USB TCP support

    def __init__(self, connection_type: str, id: str, remote_host: ipaddress.IPv4Address):

        try:
            self.__type = str(connection_type)
            self.__id = str(id)

            # verify IP

            if self._verify(remote_host):
                pass
            else:
                logging.error(f'Exception encountered during TCPConnection init - unable to verify TCP connection to {remote_host}')
                logging.error('Verify that IP is right in `constants.py` and connections are secure')
                logging.info('Beginning cleanup...')
                sys.exit()  
            
            self.__remote_host = str(ipaddress.ip_address(remote_host))
            logging.info(f"remote host {self.__remote_host}")

        except ValueError as ve:
            logging.error(f'ValueError encountered during init of TCPConnection object, {ve}')
        
        except Exception as e:
            logging.error(f'Exception encountered during init of TCPConnection object, {e}')

    def get_type(self) -> str:
        return self.__type
    
    def get_id(self) -> str:
        return self.__id    
    
    def get_remote_host_address(self) -> str:            
        return self.__remote_host

    def _verify(self, remote_host: str) -> bool:
        __download_port = constants.DEFAULT_DOWNLOAD_PORT
        __socket_handler = SocketHandler(remote_host, __download_port)
        try:
            __socket_handler.open_TCP_socket(max_attempts=5)
            logging.info(f'Connection to host {remote_host} verified')
            __socket_handler.close_TCP_socket()
            return True
        
        except Exception as e:
            return False