from core.socketHandler import SocketHandler
from core.tagHandler import tagHandler
from objects.Tag import Tag
from objects.Microcontroller import RaspberryPi
from objects.FlexEdge import FlexEdge
import sys

IP = '10.80.14.101' #change based on host
PORT = 23 # TCP Port

# simple test to demo since we don't have any hardware
def demo_test():
    socket_handler = SocketHandler(IP, PORT)
    tag_handler = tagHandler(socket_handler)

    input_tag = Tag("di_1", 0)
    output_tag = Tag("di_1", 0)
    
    print(tag_handler.get_tag_value(input_tag))

def main():
    rpi = RaspberryPi()
    rpi.set_digital_input(addr=1, val=1)


    demo_test()

if (__name__ == "__main__"):
    main()