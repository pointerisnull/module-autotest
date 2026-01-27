from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import os
import ctypes

from gui.Elements import *
from gui.Themes import *
from core.ConfigHandler import ConfigHandler
from common import constants
from gui import Popups as popup

# PyQt5 Documentation:
# https://www.riverbankcomputing.com/static/Docs/PyQt5/

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(0, 0, constants.DEFAULT_WIDTH, constants.DEFAULT_HEIGHT)
        self.dark_mode = True
        self.change_style()
        
        self.init_menu_bar()
        
        # Startup Screen
        self.container = ContainerWithBackground("./assets/hms_logo.png")
        self.setCentralWidget(self.container)
        self.startup_screen = QVBoxLayout(self.container)
        # Force welcome meathod to be below center logo
        self.startup_screen.addStretch(65) # 65%
        intro = TextBox("To start, select or create a new testing configuration.")
        self.startup_screen.addWidget(intro)
        self.startup_screen.addStretch(35) # 35%

        self.config = ConfigHandler()

    def init_menu_bar(self):
        menu_bar = self.menuBar()

        # Top-Level Menus
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        view_menu = menu_bar.addMenu("View")
        help_menu = menu_bar.addMenu("Help")

        # The '&' allows for Alt+Key shortcuts
        new_config = QAction("&New Configuration", self)
        new_config.setShortcut("Ctrl+N")
        #new_config.triggered.connect(lambda: popup.new_file(self, "New Configuration", self.config))
        new_config.triggered.connect(self.new_config)
        
        open_config = QAction("&Open Configuration", self)
        open_config.setShortcut("Ctrl+O")
        open_config.triggered.connect(lambda: print(f"{self.config.get_module()}")) # Temporary
        
        hardware_config = QAction("&Hardware Configuration", self)
        hardware_config.setShortcut("Ctrl+H")
        
        crimson_config = QAction("Configure Crimson", self)
        style_config = QAction("Change Style", self)
        style_config.triggered.connect(self.change_style)       

        exit_action = QAction("&Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        about_action = QAction("&About", self)
        about_action.setShortcut("Ctrl+A")
        about_action.triggered.connect(lambda: popup.info(self, "About", "HMS Autotester version 0.0.0"))

        # Add options to menues
        file_menu.addAction(new_config)
        file_menu.addAction(open_config)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        edit_menu.addAction(hardware_config)
        
        view_menu.addAction(crimson_config)
        view_menu.addSeparator()
        view_menu.addAction(style_config)
        
        help_menu.addAction(about_action)

    def init_UI(self):
        io_container = QHBoxLayout()
        config_container = QHBoxLayout()
        #io_list = QVBoxLayout # May not be necessary
        #config_list = QVBoxLayout() # May not be necessary

    def new_config(self):
        popup.new_file(self, "New Configuration", self.config)
        if self.config.has_changed:
            self.init_UI()

    def change_style(self):
        if self.dark_mode:
            self.setStyleSheet(LIGHT_MODE)
        else:
            self.setStyleSheet(DARK_MODE)
        self.dark_mode = not self.dark_mode
        
        # Only run on Windows
        if os.name == 'nt':
            try: 
                self.update_titlebar()
            except Exception as e:
                print(f"Could not change window theme: {e}")

    def update_titlebar(self):
        # For Windows 10 version 2004 and later, including Windows 11, it's 20.
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    
        hwnd = self.winId().__int__()
        value = ctypes.c_int(1 if self.dark_mode else 0) 
        try:
            ctypes.windll.dwmapi.DwmSetWindowAttribute(
                hwnd, 
                DWMWA_USE_IMMERSIVE_DARK_MODE, 
                ctypes.byref(value), 
                ctypes.sizeof(value)
            )
        except Exception as e:
            # Fallback for older Windows 10 versions if 20 fails
            DWMWA_USE_IMMERSIVE_DARK_MODE_OLD = 19
            ctypes.windll.dwmapi.DwmSetWindowAttribute(
                hwnd, 
                DWMWA_USE_IMMERSIVE_DARK_MODE_OLD, 
                ctypes.byref(value), 
                ctypes.sizeof(value)
            )

if __name__ == "__main__":
    # sys.argv - used to process command line arguments when program is run
    app = QApplication(sys.argv)
    window = MainWindow("HMS Module Autotester")
    window.show()

    sys.exit(app.exec_())