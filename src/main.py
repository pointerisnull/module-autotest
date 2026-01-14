from core.socketHandler import SocketHandler
from core.tagHandler import tagHandler
from objects.FlexEdge import FlexEdge

IP = '10.80.14.215' #change based on host

def main():
    socket_handler = SocketHandler(IP, 789)  

    socket_handler.open_socket()

    socket_handler.close_socket()



if (__name__ == "__main__"):
    main()