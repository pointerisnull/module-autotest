import RPi.GPIO as GPIO


class IOModule():

    def read_pin(self, pin):
        pass

    def set_pin_d(self, pin, val):
        pass

if __name__ == "main":
    io = IOModule()
    val = io.read_pin(3)