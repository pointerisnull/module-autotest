from PyQt5.QtWidgets import *

from gui.Elements import PinOption

# All IO options that can be configured
class DigitalIn(PinOption):
    def populate(self, form):
        widget = QLineEdit()
        field = "Field"
        form.addRow(field + ":", widget)

class DigitalOut(PinOption):
    def populate(self, form):
        widget = QLineEdit()
        field = "Output"
        form.addRow(field + ":", widget)

# Acts as both input and output
class DigitalMix(PinOption):
    def populate(self, form):
        widget = QLineEdit()
        field = "Field"
        form.addRow(field + ":", widget)

class AnalogIn(PinOption):
    def populate(self, form):
        widget = QLineEdit()
        field = "Field"
        form.addRow(field + ":", widget)


class AnalogOut(PinOption):
    def populate(self, form):
        widget = QLineEdit()
        field = "Field"
        form.addRow(field + ":", widget)