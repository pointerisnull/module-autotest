import RPi.GPIO as GPIO

class IOModule:
    # mode : "BCM" (GPIO #) or "BOARD" (Physical Pin #)
    def __init__(self, mode=GPIO.BOARD):
        self.mode = mode
        GPIO.setmode(self.mode)
    
    # io_mode : input by default 
    def setup_pins(pin, io_mode=GPIO.IN):
        GPIO.setup(pin, io_mode)

    def read_pin(self, pin):
        return GPIO.input(pin)

    def set_pin(self, pin, val):
        GPIO.output(pin, val)
        print(f"Setting pin {pin} to {val}")

if __name__ == "__main__":
    io = IOModule()
    io.setup_pins(12, GPIO.OUT)
    io.setup_pins(40, GPIO.IN)
    #val = io.read_pin(29)
    #print(val)
    io.set_pin(12, GPIO.HIGH)