from PyQt5.QtWidgets import *
import PyQt5.QtCore as core

from gui.Elements import PinOption
from common.constants import *

# All IO options that can be configured
class Miscellaneous(PinOption):
    def populate(self, form):
        form.setVerticalSpacing(5)
        header1 = QLabel()
        header1.setTextFormat(core.Qt.RichText)#"text-decoration: underline;")
        header1.setText("<b>Miscellaneous Settings</b>")
        form.addRow(header1)
        io_crim = QCheckBox("Compare real values with Crimson tag values")
        io_crim.setChecked(True)
        form.addRow(io_crim)
        io_iter = QLineEdit()
        io_iter.setText("1")
        form.addRow("Test iterations", io_iter)

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
        header2.setText("<b>Input Validation:</b>")
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
        header1 = QLabel()
        header1.setTextFormat(core.Qt.RichText)
        header1.setText("<b>Output Validation:</b>")
        form.addRow(header1)
        io_real = QCheckBox("Validate physical high/low")
        io_real.setChecked(True)
        form.addRow(io_real)
        io_crim = QCheckBox("Validate crimson high/low")
        io_crim.setChecked(True)
        form.addRow(io_crim)
        io_inv = QCheckBox("Inverse Logic")
        io_inv.setChecked(True)
        form.addRow(io_inv)

# Acts as both input and output
class DigitalMix(PinOption):
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
        header2.setText("<b>Input Validation:</b>")
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

        header3 = QLabel()
        header3.setTextFormat(core.Qt.RichText)
        header3.setText("<b>Output Validation:</b>")
        form.addRow(header3)
        io_real = QCheckBox("Validate physical high/low")
        io_real.setChecked(True)
        form.addRow(io_real)
        io_crim = QCheckBox("Validate crimson high/low")
        io_crim.setChecked(True)
        form.addRow(io_crim)
        io_inv = QCheckBox("Inverse Logic")
        io_inv.setChecked(True)
        form.addRow(io_inv)

class AnalogIn(PinOption):
    def populate(self, form):
        header1 = QLabel()
        header1.setText("<b>Input Voltage Extrema:</b>")
        form.addRow(header1)
        vt_max = QLineEdit()
        vt_max.setText(f"{ANALOG_VOLTAGE_MAX}")
        form.addRow("Maximum: ", vt_max)
        vt_min = QLineEdit()
        vt_min.setText(f"{ANALOG_VOLTAGE_MIN}")
        form.addRow("Minimum: ", vt_min)
        vt_tol = QLineEdit()
        vt_tol.setText(f"{VOLTAGE_TOLERANCE}")
        form.addRow("Tolerance (%):", vt_tol)

class AnalogOut(PinOption):
    def populate(self, form):
        header1 = QLabel()
        header1.setText("<b>Output Voltage Extrema:</b>")
        form.addRow(header1)
        vt_max = QLineEdit()
        vt_max.setText(f"{ANALOG_VOLTAGE_MAX}")
        form.addRow("Maximum: ", vt_max)
        vt_min = QLineEdit()
        vt_min.setText(f"{ANALOG_VOLTAGE_MIN}")
        form.addRow("Minimum: ", vt_min)
        vt_tol = QLineEdit()
        vt_tol.setText(f"{VOLTAGE_TOLERANCE}")
        form.addRow("Tolerance (%):", vt_tol)

class ThermocoupleInput(PinOption):
    def populate(self, form):
        header1 = QLabel()
        header1.setText("<b>RTD/TC Input:</b>")
        form.addRow(header1)
        '''
        tc_type, tc_type_okay = QInputDialog.getItem(
                self, 
                "Module Type", 
                "Select module for this config:", 
                TC_TYPES, 
                0, 
                False
            )
        '''



class ExcitationInput(PinOption):
    def populate(self, form):
        header1 = QLabel()
        header1.setText("<b>RTD +EXC Input:</b>")
        form.addRow(header1)


def get_module_io(module_type, io_list, options_stack):
    #TODO
    # THIS IS TERRIBLE, PLEASE REWRITE LATER!!!
    misc_tab = Miscellaneous("Miscellaneous Settings")
    io_list.addItem("Miscellaneous Settings")
    options_stack.addWidget(misc_tab.get_contents())

    #8DI/8DO
    if module_type == MODULES[0]:
        for i in range(1, 9):
            io_tab = DigitalIn(f"DI_{i}")
            io_list.addItem(f"DI_{i}")
            options_stack.addWidget(io_tab.get_contents())
        for i in range(1, 9):
            io_tab = DigitalOut(f"DO_{i}")
            io_list.addItem(f"DO_{i}")
            options_stack.addWidget(io_tab.get_contents())

    #2uin
    if module_type == MODULES[2]:
        for i in range(2):
            tc_tab = ThermocoupleInput(f"TC/RTD+ ({i+1})")
            ext_tab = ExcitationInput(f"RTD+EXC ({i+1})")
            volt_tab = AnalogIn(f"0-10v ({i+1})")
            curr_tab = AnalogIn(f"4-20mA ({i+1})")
            io_list.addItem(f"TC/RTD+ ({i+1})")
            io_list.addItem(f"RTD+EXC ({i+1})")
            io_list.addItem(f"0-10v ({i+1})")
            io_list.addItem(f"4-20mA ({i+1})")
            options_stack.addWidget(tc_tab.get_contents())
            options_stack.addWidget(ext_tab.get_contents())
            options_stack.addWidget(volt_tab.get_contents())
            options_stack.addWidget(curr_tab.get_contents())
        for i in range(2):
            volt_tab = AnalogOut(f"V+ ({i+1})")
            curr_tab = AnalogOut(f"I+ ({i+1})")
            io_list.addItem(f"V+ ({i+1})")
            io_list.addItem(f"I+ ({i+1})")
            options_stack.addWidget(volt_tab.get_contents())
            options_stack.addWidget(curr_tab.get_contents())
        for i in range(1, 9):
            io_tab = DigitalMix(f"DI/DO ({i})")
            io_list.addItem(f"DI/DO ({i})")
            options_stack.addWidget(io_tab.get_contents())
    #4uin
    if module_type == MODULES[3]:
        for i in range(4):
            tc_tab = ThermocoupleInput(f"TC/RTD+ ({i+1})")
            ext_tab = ExcitationInput(f"RTD+EXC ({i+1})")
            volt_tab = AnalogIn(f"0-10v ({i+1})")
            curr_tab = AnalogIn(f"4-20mA ({i+1})")
            io_list.addItem(f"TC/RTD+ ({i+1})")
            io_list.addItem(f"RTD+EXC ({i+1})")
            io_list.addItem(f"0-10v ({i+1})")
            io_list.addItem(f"4-20mA ({i+1})")
            options_stack.addWidget(tc_tab.get_contents())
            options_stack.addWidget(ext_tab.get_contents())
            options_stack.addWidget(volt_tab.get_contents())
            options_stack.addWidget(curr_tab.get_contents())
        for i in range(2):
            volt_tab = AnalogOut(f"V+ ({i+1})")
            curr_tab = AnalogOut(f"I+ ({i+1})")
            io_list.addItem(f"V+ ({i+1})")
            io_list.addItem(f"I+ ({i+1})")
            options_stack.addWidget(volt_tab.get_contents())
            options_stack.addWidget(curr_tab.get_contents())
        for i in range(1, 4):
            io_tab = DigitalMix(f"DI/DO ({i})")
            io_list.addItem(f"DI/DO ({i})")
            options_stack.addWidget(io_tab.get_contents())

    # 6uin
    if module_type == MODULES[4]:
        for i in range(6):
            tc_tab = ThermocoupleInput(f"TC/RTD+ ({i+1})")
            ext_tab = ExcitationInput(f"RTD+EXC ({i+1})")
            volt_tab = AnalogIn(f"0-10v ({i+1})")
            curr_tab = AnalogIn(f"4-20mA ({i+1})")
            io_list.addItem(f"TC/RTD+ ({i+1})")
            io_list.addItem(f"RTD+EXC ({i+1})")
            io_list.addItem(f"0-10v ({i+1})")
            io_list.addItem(f"4-20mA ({i+1})")
            options_stack.addWidget(tc_tab.get_contents())
            options_stack.addWidget(ext_tab.get_contents())
            options_stack.addWidget(volt_tab.get_contents())
            options_stack.addWidget(curr_tab.get_contents())