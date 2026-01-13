import RPi.GPIO as GPIO

class IOModule():
    # mode : "BCM" (GPIO #) or "BOARD" (Physical Pin #)
    def __init__(self, mode=GPIO.BOARD):
        self.mode = mode
        GPIO.setmode(self.mode)
    
    # io_mode : input by default 
    def setup_pins(pins, io_mode=GPIO.IN):
        print("HERE!!")
        for i in len(pins):
            GPIO.setup(pins[i], io_mode)

    def read_pin(self, pin):
        return GPIO.input(pin)

    def set_pin(self, pin, val):
        GPIO.output(pin, val)
        print(f"Setting pin {pin} to {val}")

if __name__ == "main":
    io = IOModule()
    io.setup_pins([12, 11], GPIO.OUT)
    io.setup_pins([38, 40], GPIO.IN)
    #val = io.read_pin(29)
    #print(val)
    io.set_pin(12, GPIO.HIGH)