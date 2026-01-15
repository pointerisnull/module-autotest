import RPi.GPIO as GPIO
import time
import os
import csv
import utils.FileIO as FileIO

PINOUT_SETTINGS_PATH = "./settings/pinout.csv"

class RaspberryPi:
    def __init__(self):
        self.pins = self.get_pinout()
        self.io = IOModule(self.pins['MODE'])
        # pi output -> module input
        self.io.setup_pins(self.pins['di_x'], GPIO.OUT)
        # pi input <- module output
        self.io.setup_pins(self.pins['do_x'], GPIO.IN)
        # setup address pins, will always be output
        self.io.setup_pins(self.pins['di_a'], GPIO.OUT)
        self.io.setup_pins(self.pins['di_b'], GPIO.OUT)
        self.io.setup_pins(self.pins['di_c'], GPIO.OUT)
        self.io.setup_pins(self.pins['do_a'], GPIO.OUT)
        self.io.setup_pins(self.pins['do_b'], GPIO.OUT)
        self.io.setup_pins(self.pins['do_c'], GPIO.OUT)
    
    def get_pinout(self):
        # read pinout.csv
        return FileIO.read_csv_config(PINOUT_SETTINGS_PATH, 'FUNCTION', 'PIN')
        '''
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
        '''

    def get_binary_address(self, addr):
        return [int(bit) for bit in f'{addr:03b}']

    # via demux common pin
    def set_digital_input(self, addr=1, val=GPIO.HIGH):
        bin_addr = self.get_binary_address(addr)
        input_pin = self.pins['di_x']

        self.io.set_pin(self.pins['di_a'], bin_addr[0])
        self.io.set_pin(self.pins['di_b'], bin_addr[1])
        self.io.set_pin(self.pins['di_c'], bin_addr[2])

        self.io.set_pin(input_pin, val)

    # via mux common pin
    def read_digital_output(self, addr=1):
        bin_addr = self.get_binary_address(addr)
        output_pin = self.pins['do_x']
        
        self.io.set_pin(self.pins['di_a'], bin_addr[0])
        self.io.set_pin(self.pins['di_b'], bin_addr[1])
        self.io.set_pin(self.pins['di_c'], bin_addr[2])

        val = self.io.read_pin(output_pin)
        return val

class IOModule:
    # mode : "BCM" (GPIO #) or "BOARD" (Physical Pin #)
    def __init__(self, mode='BOARD'):
        if mode == 'BOARD':
            self.mode = GPIO.BOARD
        else:
            self.mode = GPIO.BCM
        GPIO.setmode(self.mode)
    
    # io_mode : input by default 
    def setup_pins(self, pin, io_mode=GPIO.IN):
        GPIO.setup(pin, io_mode)

    def read_pin(self, pin):
        return GPIO.input(pin)

    def set_pin(self, pin, val):
        GPIO.output(pin, val)

    def shutdown(self):
        GPIO.cleanup()

if __name__ == "__main__":
    rpi = RaspberryPi()
    
    rpi.set_digital_input(1, 1)

    while(1):
        rpi.set_digital_input(1, 1)
        time.sleep(1)
        rpi.set_digital_input(1, 0)
        time.sleep(1)
        print(f"Output Pin: {rpi.read_digital_output(1)}")