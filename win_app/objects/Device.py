from objects.connections import TCPConnection

class Device:

    def __init__(self, device_id: str, configured_connections: list[TCPConnection]):

        self.__device_id = device_id
        self.__configured_connections_list = configured_connections

    def get_device_id(self) -> str:
        return self.__device_id()
    
    def get_configured_connections_list(self) -> list[TCPConnection]:
           
        return self.__configured_connections_list
    
    def append_configured_connections_list(self, connection: TCPConnection) -> None:
        self.__configured_connections_list.append(connection)
        if isinstance(connection, TCPConnection):
            if self.get_tcp_connection() == None:
                self.__tcp_connection = connection

    def get_tcp_connection(self) -> TCPConnection | None:
        
        return self.__tcp_connection
    
    def __find_tcp_connection(self) -> TCPConnection:
        
        for configured_connection in self.get_configured_connections_list():
            if type(configured_connection) == TCPConnection:
                return configured_connection