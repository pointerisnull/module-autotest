from core.socketHandler import SocketHandler
from core.tagHandler import tagHandler
from objects.Tag import Tag

IP = '10.80.14.215' #change based on host

def main():
    socket_handler = SocketHandler(IP, 502)
    tag_handler = tagHandler(socket_handler)
    tag = Tag("DI_1", 0)

    print(tag_handler.get_tag_value(tag))

if (__name__ == "__main__"):
    main()