from core.socketHandler import SocketHandler
from core.tagHandler import TagHandler

class FlexEdge:
    def __init__(self, ip_addr: str, port: int):
        self.address = ip_addr
        self.port = port
        self.socket_handler = SocketHandler(self.address, self.port)
        self.tag_handler = TagHandler(self.socket_handler)
    
    def connect(self):
        self.socket_handler.open_TCP_socket()

    def reconnect(self):
        self.socket_handler.reset_TCP_socket()
    
    def disconnect(self):
        self.socket_handler.close_TCP_socket()

    def upload_database(self, db_path: str):
        pass

    def download_device_database(self, destination_path: str):
        pass

    def get_tag(self, tag_label: str):
        pass

    def get_tag_val(self, tag_label: str):
        pass

    def set_tag_val(self, tag_label:str, val):
        pass

