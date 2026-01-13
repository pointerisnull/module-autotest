import RPi.GPIO as GPIO
import time

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

if __name__ == "__main__":
    di_1 = 12
    do_1 = 40

    io = IOModule()
    io.setup_pins(di_1, GPIO.OUT)
    io.setup_pins(do_1, GPIO.IN)

    while(1):
        io.set_pin(di_1, GPIO.HIGH)
        time.sleep(1)
        io.set_pin(di_1, GPIO.LOW)
        time.sleep(1)
        print(f"Pin {do_1}: {io.read_pin(do_1)}")