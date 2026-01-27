import socket
import time 
import logging
import sys
from logging import Logger
from common import constants

DEFAULT_SOCKET_TIMEOUT = 2
DEFAULT_FIND_ATTEMPTS = 5

class SocketHandler:
    def __init__(self, remote_host_address: str, debug_port: int):
        self.__remote_host_address = str(remote_host_address)
        self.__socket = None
        self.__debug_port = int(debug_port)

    def get_remote_host_address(self):
        return self.__remote_host_address

    def get_socket(self):
        return self.__socket 
    
    def open_socket(self, max_attempts: int=DEFAULT_FIND_ATTEMPTS):
        __TIMEOUT = DEFAULT_SOCKET_TIMEOUT
        __attempts = 0 

        while __attempts < max_attempts:
            print(f'Attempting to open TCP socket.... attempt {__attempts + 1}/{max_attempts}')
            time.sleep(2)
            try:
                self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__socket.settimeout(constants.BACKOFF_BASE ** __TIMEOUT)
                self.__socket.connect((self.__remote_host_address, self.__debug_port))
                break
            
            except TimeoutError as e:
                logging.error(f'TimeoutError while attempting to open socket: {e}')
            except ConnectionRefusedError as e:
                logging.error(f'ConnectionRefusedError while attempting to open socket: {e}')

            __attempts += 1
            continue
        
        if __attempts >= max_attempts:
            logging.critical("Unable to communicate with device")
            raise Exception
        
        logging.info(f'Connection established with {self.__remote_host_address}')

    def close_socket(self):
        try:
            self.__socket.close()
        except Exception as e:
            logging.error(f'Error occurred while attempting to close socket: {e}')
        finally:
            self.__socket = None
            logging.info(f'Socket successfully closed')
    
    def reset_socket(self):
            self.close_socket() 
            self.open_socket()

    def flush_socket(self) -> None:
        if self.__socket is None:
            logging.warning("Socket not open. Opening to be flushed...")
            self.open_socket()
            
        sock = self.get_socket()    
        if sock is None:
            return
        
        sock.setblocking(False)

        try: 
            while True:
                data = sock.recv(2048)
                if not data:
                    break
        except BlockingIOError:
            pass
        finally:
            sock.setblocking(True)
