from core.socketHandler import SocketHandler
from core.tagHandler import tagHandler
from objects.Tag import Tag
import sys

IP = '10.80.14.101' #change based on host
PORT = 789 # TCP Port

def main():
    socket_handler = SocketHandler(IP, PORT)
    tag_handler = tagHandler(socket_handler)
    tag = Tag("Tag1", 0)
    '''
    try:
        socket_handler.open_socket()
    except Exception as e:
        print(e)
        sys.exit()
    '''

    print(tag_handler.get_tag_value(tag))

if (__name__ == "__main__"):
    main()