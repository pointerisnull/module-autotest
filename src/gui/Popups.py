from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import common.constants as constants

def about(window, title, msg):
    QMessageBox.about(window, title, msg)

def confirm_action(self, title, message):
    reply = QMessageBox.question(
        self, 
        title, 
        message,
        QMessageBox.Yes | QMessageBox.No, 
        QMessageBox.No  # This sets the default highlighted button
    )

    return reply == QMessageBox.Yes

# Create new configuration file in config_handler's set directory
def new_file(window, title, config_handler):

    window_flags = Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint 
    user_input, ok = QInputDialog.getText(window, title, 'Enter file name:', QLineEdit.Normal, "untitled", window_flags)
    
    if ok and user_input:
        # First ask for the Module Type
        module_type, ok_module = QInputDialog.getItem(
            window, 
            "Module Type", 
            "Select module for this config:", 
            constants.MODULES, 
            0, 
            False, 
            window_flags
        )
        if ok_module:
            print(f"Creating config {user_input} for {module_type} module")
            try:
                config_handler.create_config(user_input, module_type=module_type, overwrite=False)
                config_handler.set_config(user_input)
                config_handler.has_changed = True
                QMessageBox.information(window, "Success", f"File '{user_input}' created!")

            except FileExistsError:
                action = confirm_action(window, "File IO", "Configuration already exists. Replace?")
                if action:
                    config_handler.create_config(user_input, module_type=module_type, overwrite=True)
                    config_handler.set_config(user_input)
                    config_handler.has_changed = True
                    QMessageBox.information(window, "Success", f"File '{user_input}' created!")

# Module hardware configuration: select which slot will run which configuration
def hardware_config(window, config_handler):
    dialog = QDialog(window)
    dialog.setWindowTitle("Module Configuration")
    dialog.setFixedSize(350, 250) 
    
    # Flags to clean up the window's frame
    dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    # Apply main window theme
    dialog.setStyleSheet(window.styleSheet())

    layout = QVBoxLayout(dialog)
    form = QFormLayout()
    dropdowns = []

    options = config_handler.list_configs()
    if "Empty" not in options:
        options.insert(0, "Empty")

    for i in range(4):
        combo = QComboBox()
        combo.addItems(options)
        
        index = combo.findText("Empty")
        if index >= 0:
            combo.setCurrentIndex(index)
            
        form.addRow(f"Module Slot {i}:", combo)
        dropdowns.append(combo)

    layout.addLayout(form)

    buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    layout.addWidget(buttons)

    buttons.accepted.connect(dialog.accept)
    buttons.rejected.connect(dialog.reject)

    if dialog.exec_() == QDialog.Accepted:
        results = [cb.currentText() for cb in dropdowns]
        return results
    
    return None