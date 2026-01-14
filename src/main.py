from core.socketHandler import SocketHandler
from core.tagHandler import tagHandler
from objects.Tag import Tag

IP = '10.80.14.215' #change based on host

def main():
    tag_handler = tagHandler()
    tag = Tag("DI_1", 0)

    tag_handler.get_tag_value(tag)

if (__name__ == "__main__"):
    main()