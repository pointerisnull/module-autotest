from PyQt5.QtWidgets import *
import PyQt5.QtCore as core

from gui.Elements import PinOption
from gui.Elements import TextBox
from common.constants import *

# All IO options that can be configured
class DigitalIn(PinOption):
    def populate(self, form):
        form.setVerticalSpacing(5)
        header1 = QLabel()
        header1.setTextFormat(core.Qt.RichText)#"text-decoration: underline;")
        header1.setText("<b>High Voltage Threshold:</b>")
        form.addRow(header1)
        vt_max = QLineEdit()
        vt_max.setText(f"{HIGH_VOLTAGE_MAX}")
        form.addRow("Maximum: ", vt_max)
        vt_min = QLineEdit()
        vt_min.setText(f"{HIGH_VOLTAGE_MIN}")
        form.addRow("Minimum: ", vt_min)
        vt_exp = QLineEdit()
        vt_exp.setText(f"{HIGH_VOLTAGE_EXP}")
        form.addRow("Expected: ", vt_exp)
        vt_tol = QLineEdit()
        vt_tol.setText(f"{VOLTAGE_TOLERANCE}")
        form.addRow("Tolerance (%):", vt_tol)

        header1_1 = QLabel()
        header1_1.setTextFormat(core.Qt.RichText)#"text-decoration: underline;")
        header1_1.setText("<b>Low Voltage Threshold:</b>")
        form.addRow(header1_1)
        vtl_max = QLineEdit()
        vtl_max.setText(f"{LOW_VOLTAGE_MAX}")
        form.addRow("Maximum: ", vtl_max)
        vtl_min = QLineEdit()
        vtl_min.setText(f"{LOW_VOLTAGE_MIN}")
        form.addRow("Minimum: ", vtl_min)
        vtl_exp = QLineEdit()
        vtl_exp.setText(f"{LOW_VOLTAGE_EXP}")
        form.addRow("Expected: ", vtl_exp)
        vtl_tol = QLineEdit()
        vtl_tol.setText(f"{VOLTAGE_TOLERANCE}")
        form.addRow("Tolerance (%):", vtl_tol)

        header2 = QLabel()
        header2.setTextFormat(core.Qt.RichText)
        header2.setText("<b>IO Validation:</b>")
        form.addRow(header2)
        io_real = QCheckBox("Validate physical high/low")
        io_real.setChecked(True)
        form.addRow(io_real)
        io_crim = QCheckBox("Validate crimson high/low")
        io_crim.setChecked(True)
        form.addRow(io_crim)
        io_inv = QCheckBox("Inverse Logic")
        io_inv.setChecked(False)
        form.addRow(io_inv)

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