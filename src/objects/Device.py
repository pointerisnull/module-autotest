from core.socketHandler import SocketHandler
from core.tagHandler import tagHandler
from objects.Tag import Tag

# Class for Crimson device
class Device:
    def __init__(self, ip_addr: str, port: int):
        self.address = ip_addr
        self.port = port
        self.socket_handler = SocketHandler(self.address, self.port)
        self.tag_handler = tagHandler(self.socket_handler)
    
    def connect(self):
        self.socket_handler.open_socket()

    def reconnect(self):
        self.socket_handler.reset_socket()
    
    def disconnect(self):
        self.socket_handler.close_socket()

    def upload_database(self, db_path: str):
        pass

    def download_device_database(self, destination_path: str):
        pass

    def get_tag(self, tag_label: str):
        tg = Tag(tag_label, 0)
        return self.tag_handler.get_tag_value(tg)

    def set_tag_val(self, tag_label:str, val):
        pass

