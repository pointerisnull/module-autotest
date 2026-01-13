import RPi.GPIO as GPIO

class IOModule():
    # mode : "BCM" (GPIO #) or "BOARD" (Physical Pin #)
    def __init__(self, mode=GPIO.BCM):
        self.mode = mode
        GPIO.setmode(self.mode)
    
    # io_mode : input by default 
    def setup_pins(pins, io_mode=GPIO.IN):
        for i in len(pins):
            GPIO.setup(pins[i], io_mode)

    def read_pin(self, pin):
        return GPIO.input(pin)

    def set_pin(self, pin, val):
        GPIO.output(pin, val)

if __name__ == "main":
    io = IOModule()
    io.setup_pins([15, 16], GPIO.OUT)
    io.setup_pins([28, 29], GPIO.IN)
    #val = io.read_pin(29)
    #print(val)
    io.set_pin(15, GPIO.LOW)
