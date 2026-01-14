from core.socketHandler import SocketHandler
from core.tagHandler import tagHandler
from objects.Tag import Tag

IP = '10.80.14.215' #change based on host
PORT = 23

def main():
    socket_handler = SocketHandler(IP, PORT)
    socket_handler.open_socket()

    tag_handler = tagHandler(socket_handler)
    tag = Tag("DI_1", 0)

    print(tag_handler.get_tag_value(tag))

if (__name__ == "__main__"):
    main()