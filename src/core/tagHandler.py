import sys
import time
import logging

from core.socketHandler import SocketHandler
from objects.Tag import Tag

DEFAULT_ATTEMPTS = 10

class tagHandler:
    def __init__(self, socket_handler: SocketHandler):
        self.__socket_handler = socket_handler
    
    def get_socket_handler(self):
        return self.__socket_handler
    
    def get_tag_value(self, tag: Tag) -> str | int:
        try:
            __target_data = None
            __response = self.__get_raw_tag_data(tag)
            __response_lines = __response.split('\r\n')
            for line in __response_lines:
                if '=' in line:
                    __line_split = line.split('=')
                    __target_data = (__line_split[1]).replace(' ','')
                elif 'tag not found' in line:
                    logging.error(f'Unable to find tag "{tag.get_tag_name()}" on device')
                    logging.info("Ensure that device is configured with the proper tags CHANGE THIS LATER")
            if __target_data.isdigit():
                return int(__target_data)
            else:
                return __target_data
        except Exception as e:
            logging.error(f'Unexpected exception encountered while trying to get "{tag.get_tag_name()}" tag value from device, {e}')
  
    def __get_raw_tag_data(self, tag: Tag):
        __attempts = DEFAULT_ATTEMPTS
        while __attempts > 0:
            try:
                self.__send_command(self.__format_tag_command(tag, 'get'))
                __response = self.__get_device_response(tag)
                return __response

            except TimeoutError as te:
                logging.error(f'TimeoutError while attempting to get raw "{tag.get_tag_name()}" tag data from device, {te}')
                time.sleep(5)
                __attempts -= 1
                self.__socket_handler.reset_socket()
                logging.info(f'Reattempting to get device response, {__attempts}/10 attempts remaining')

                continue
        
        logging.critical("Failed to get response from device")
        logging.info("Verify device connection and config")
        logging.info('Exiting.')
        sys.exit()

    def __format_tag_command(self, tag: Tag, action: str):
        match action:
            case 'get':
                return f'tags.get {tag.get_tag_name()}\r\n'
            
    def __send_command(self, formatted_command: str):
        self.__socket_handler.flush_socket()
        try:
            self.__socket_handler.get_socket().sendall(formatted_command.encode())
        except Exception as e:
            logging.error(f'Command failed, {e}')

    def __get_device_response(self, tag: Tag):
        __buffer = ''
        __tag_name = tag.get_tag_name()
        while True:
            __response = self.__socket_handler.get_socket().recv(2048).decode('utf-8', errors='replace')
            __buffer += __response
            if __tag_name in __buffer:
                break
            else:
                __buffer =''
        return __response