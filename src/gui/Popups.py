from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import common.constants as constants
from gui import Window as win

class PopupManager:
    def __init__(self, dark_mode=False):
        self.dark_mode = dark_mode

    def change_style(self):
        self.dark_mode = not self.dark_mode

    def about(self, parent, title, msg):
        newwin = QMessageBox()
        win.update_titlebar(newwin, self.dark_mode)
        newwin.about(parent, title, msg)
    
    def confirm_action(self, parent, title, message):
        #win.update_titlebar(self, self.dark_mode)
        reply = QMessageBox.question(
            parent, 
            title, 
            message,
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  # This sets the default highlighted button
        )
    
        return reply == QMessageBox.Yes
    
    # Create new configuration file in config_handler's set directory
    def new_file(self, parent, title, config_handler):
        #win.update_titlebar(self, self.dark_mode)
    
        window_flags = Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint 
        user_input, ok = QInputDialog.getText(parent, title, 'Enter file name:', QLineEdit.Normal, "untitled", window_flags)
        
        if ok and user_input:
            # First ask for the Module Type
            module_type, ok_module = QInputDialog.getItem(
                parent, 
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
                    QMessageBox.information(parent, "Success", f"File '{user_input}' created!")
    
                except FileExistsError:
                    action = self.confirm_action(parent, "File IO", "Configuration already exists. Replace?")
                    if action:
                        config_handler.create_config(user_input, module_type=module_type, overwrite=True)
                        config_handler.set_config(user_input)
                        config_handler.has_changed = True
                        QMessageBox.information(parent, "Success", f"File '{user_input}' created!")
    
    # Module hardware configuration: select which slot will run which configuration
    def hardware_config(self, parent, config_handler):
        #win.update_titlebar(self, self.dark_mode)
        dialog = QDialog(parent)
        dialog.setWindowTitle("Module Configuration")
        dialog.setFixedSize(350, 250) 
        
        # Flags to clean up the window's frame
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
    
        # Apply main window theme
        dialog.setStyleSheet(parent.styleSheet())
    
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