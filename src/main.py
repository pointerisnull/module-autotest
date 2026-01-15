from objects.Microcontroller import RaspberryPi
from objects.Device import Device
import utils.FileIO as FileIO
import time

CONFIG_PATH = "./settings/device_config.csv"

def validate(inpt, crimson_in, crimson_out, out):
    if inpt == crimson_in == crimson_out == out:
        return True
    return False

# simple test to demo since we don't have any hardware
def simple_test(rpi, flexedge):
    true_signal = 1
    passc = 0
    try:
        for i in range(1000):
            rpi.set_digital_input(addr=1, val=true_signal)
            time.sleep(0.1)
            input_tag_val = flexedge.get_tag("di_1")
            output_tag_val = flexedge.get_tag("do_1")
            time.sleep(0.1)
            true_output = rpi.read_digital_output(addr=1)
            
            print(f"Itteration {i}")
            print(f"Actual Input: {true_signal}")
            print(f"Crimson Input: {input_tag_val}")
            print(f"Crimson Output: {output_tag_val}")
            print(f"Actual Output: {true_output}")

            if validate(true_signal, input_tag_val, output_tag_val, true_output):
                passc += 1
                print("Test Passed\n")
            else:
                print("Test Failed.")

            true_signal = not true_signal

    except Exception as e:
        print(f"Test Terminated. Reason: {e}")
    
    print(f"Test Completed. Itterations validated: {passc}")

def main():
    rpi = RaspberryPi()

    IP = FileIO.read_csv_setting(CONFIG_PATH, "IP Address")
    PORT = FileIO.read_csv_setting(CONFIG_PATH, "TCP Port") 
    flexedge = Device(IP, PORT)

    simple_test(rpi, flexedge)

if (__name__ == "__main__"):
    main()