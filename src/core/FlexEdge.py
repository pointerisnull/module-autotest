from socketHandler import SocketHandler

class FlexEdge:
    def __init__(self, ip_addr: str, port: int):
        self.address = ip_addr
        self.port = port
        self.socket_handler = SocketHandler(self.address, self.port)
    
    def connect(self):
        pass

    def disconnect(self):
        pass

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

