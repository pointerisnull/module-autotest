from core.socketHandler import SocketHandler
from core.tagHandler import tagHandler
from objects.Tag import Tag
from objects.Microcontroller import RaspberryPi
from objects.FlexEdge import FlexEdge
import utils.FileIO as FileIO

CONFIG_PATH = "./settings/device_config.csv"

# simple test to demo since we don't have any hardware
def demo_test(rpi, flexedge):
    rpi.set_digital_input(addr=1, val=1)
    
    print(flexedge.get_tag("di_1"))
    print(flexedge.get_tag("do_1"))

def main():
    rpi = RaspberryPi()

    IP = FileIO.read_csv_setting(CONFIG_PATH, "IP Address")
    PORT = FileIO.read_csv_setting(CONFIG_PATH, "TCP Port") 
    fe = FlexEdge(IP, PORT)

    demo_test(rpi, fe)

if (__name__ == "__main__"):
    main()