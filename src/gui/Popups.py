from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from core import ConfigHandler

def info(window, title, msg):
    QMessageBox.about(window, title, msg)

def new_file(window, title, config_handler):
    window_flags = Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint 
    user_input, ok = QInputDialog.getText(window, title, 'Enter file name:', QLineEdit.Normal, "untitled", window_flags)
    
    if ok and user_input:
        # Here config is created
        print(f"Creating file: {user_input}")
        QMessageBox.information(window, "Success", f"File '{user_input}' created!")
        config_handler.create_config(user_input)
        config_handler.set_config(user_input)
        config_handler.has_changed = True

def hardware_config(window, config_handler):
    pass
