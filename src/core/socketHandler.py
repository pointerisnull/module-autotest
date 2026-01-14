import socket
import time 
import logging
import sys


HOST = "127.0.0.1"
PORT = 687

class SocketHandler:
    def __init__(self, remote_host_address: str, debug_port: int):
        self.__remote_host_address = str(remote_host_address)
        self.__socket = None
        self.__debug_port = int(debug_port)

    def get_remote_host_address(self):
        return self.__remote_host_address

    def get_socket(self):
        return self.__socket 
    
    def open_socket(self, max_attempts = 5):
        __TIMEOUT = 2
        __attempts = 0 


        while __attempts < max_attempts:
            try:
                self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__socket.settimeout(__TIMEOUT)
                self.__socket.connect((self.__remote_host_address, self.__debug_port))
                break
            
            except TimeoutError as e:
                logging.Logger.log('error',f'TimeoutError while attempting to open socket: {e}')
            except ConnectionRefusedError as e:
                logging.Logger.log('error',f'ConnectionRefusedError while attempting to open socket: {e}')

            __attempts += 1
            continue
        
        if __attempts >= max_attempts:
            logging.log('critical', "Unable to communicate with device")
            raise Exception
        
        # best case: connection established
        logging.log('info', f'Connection established with {self.__remote_host_address}')

    def close_socket(self):
        try:
            self.__socket.close()

        except Exception as e:
            logging.log('error', f'Error occurred while attempting to close socket: {e}')
        
        logging.log('info', f'Socket successfully closed')
        return
    
    def reset_socket(self):
            self.close_socket() 
            self.open_socket()

    def flush_socket(self):
        sock = self.get_socket()
        sock.setblocking(False)

        while True:
            data = sock.recv(2048)
            if not data:
                break

        sock.setblocking(True)
