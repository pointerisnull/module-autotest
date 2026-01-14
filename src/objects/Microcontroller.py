import RPi.GPIO as GPIO
import time
import os
import csv

PINOUT_SETTINGS_PATH = "./settings/pinout.csv"

class RaspberryPi:
    def __init__(self):
        self.pin_config = self.get_pinout()
        self.io = IOModule(self.pin_config['MODE'])
        # pi output -> module input
        self.io.setup_pins(self.pin_config['di_x'], GPIO.OUT)
        # pi input <- module output
        self.io.setup_pins(self.pin_config['do_x'], GPIO.IN)
        # setup address pins, will always be output
        self.io.setup_pins(self.pin_config['di_a'], GPIO.OUT)
        self.io.setup_pins(self.pin_config['di_b'], GPIO.OUT)
        self.io.setup_pins(self.pin_config['di_c'], GPIO.OUT)
        self.io.setup_pins(self.pin_config['do_a'], GPIO.OUT)
        self.io.setup_pins(self.pin_config['do_b'], GPIO.OUT)
        self.io.setup_pins(self.pin_config['do_c'], GPIO.OUT)
    
    def get_pinout(self):
       # read pinout.csv
       file_path = PINOUT_SETTINGS_PATH
       if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

       config_dict = {}
    
       with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
        
            for row in reader:
                function_name = row['FUNCTION'].strip()
                pin_raw = row['PIN'].strip()
            
                try:
                    # Attempt to convert to integer
                    pin_value = int(pin_raw)
                except ValueError:
                    # Fallback to string if it's not an integer
                    pin_value = pin_raw
                config_dict[function_name] = pin_value
       return config_dict

    def get_binary_address(self, addr):
        return [int(bit) for bit in f'{addr:03b}']

    # via demux common pin
    def set_digital_input(self, addr, val=GPIO.IN):
        bin_addr = self.get_binary_address(addr)
        input_pin = self.pin_config['di_x']

    # via mux common pin
    def get_digital_output(self, addr):
        bin_addr = self.get_binary_address(addr)
        output_pin = self.pin_config['do_x']

class IOModule:
    # mode : "BCM" (GPIO #) or "BOARD" (Physical Pin #)
    def __init__(self, mode=GPIO.BOARD):
        self.mode = mode
        GPIO.setmode(self.mode)
    
    # io_mode : input by default 
    def setup_pins(self, pin, io_mode=GPIO.IN):
        GPIO.setup(pin, io_mode)

    def read_pin(self, pin):
        return GPIO.input(pin)

    def set_pin(self, pin, val):
        GPIO.output(pin, val)
        #print(f"Setting pin {pin} to {val}")

    def shutdown(self):
        GPIO.cleanup()

if __name__ == "__main__":
    rpi = RaspberryPi()
    print(rpi.get_pinout())
    print(rpi.get_binary_address(3))
    rpi.set_digital_input(1, 1)
    
    #io = IOModule()
    #io.setup_pins(di_1, GPIO.OUT)
    #io.setup_pins(do_1, GPIO.IN)

    while(1):
        #io.set_pin(di_1, GPIO.HIGH)
        time.sleep(1)
        #io.set_pin(di_1, GPIO.LOW)
        time.sleep(1)
        #print(f"Pin {do_1}: {io.read_pin(do_1)}")