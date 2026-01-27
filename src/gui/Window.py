from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

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
        self.setWindowIcon(QIcon("./assets/icon.png"))
        self.center_on_screen()

        self.config = ConfigHandler()
        
        self.dark_mode = True
        self.popup = popup.PopupManager(self.dark_mode)
        self.change_style()
        

        self.init_menu_bar()
    
        # Startup Screen
        self.container = ContainerWithBackground("./assets/rl_logo.png")
        self.setCentralWidget(self.container)
        self.startup_screen = QVBoxLayout(self.container)
        # Force welcome meathod to be below center logo
        self.startup_screen.addStretch(65) # 65%
        intro = TextBox("To start, open or create a new testing configuration.")
        self.startup_screen.addWidget(intro)
        self.startup_screen.addStretch(35) # 35%
    
    def center_on_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()  # Center point of screen
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
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
        open_config.triggered.connect(self.init_UI) # Temporary
        
        hardware_config = QAction("&Hardware Configuration", self)
        hardware_config.triggered.connect(lambda: self.popup.hardware_config(self, self.config))
        hardware_config.setShortcut("Ctrl+H")
        
        crimson_config = QAction("Configure Crimson", self)
        style_config = QAction("&Change Style", self)
        style_config.setShortcut("Ctrl+Shift+D")
        style_config.triggered.connect(self.change_style)       

        exit_action = QAction("&Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        about_action = QAction("&About", self)
        about_action.setShortcut("Ctrl+A")
        about_action.triggered.connect(lambda: self.popup.about(self, "About", "HMS Autotester version 0.0.0"))

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
        self.container.deleteLater()
        self.container = QWidget()
        self.setCentralWidget(self.container)

        io_container = QHBoxLayout(self.container)
        io_container.addWidget(TextBox("IO CONTAINER"))
        config_container = QHBoxLayout(self.container)
        config_container.addWidget(TextBox("CONFIG CONTAINER"))
        #io_list = QVBoxLayout # May not be necessary
        #config_list = QVBoxLayout() # May not be necessary

    def new_config(self):
        self.popup.new_file(self, "New Configuration", self.config)
        if self.config.has_changed:
            self.init_UI()

    def change_style(self):
        if self.dark_mode:
            self.setStyleSheet(LIGHT_MODE)
        else:
            self.setStyleSheet(DARK_MODE)
        self.dark_mode = not self.dark_mode
        self.popup.change_style()
        
        update_titlebar(self, self.dark_mode)

def update_titlebar(target_widget, is_dark_mode):
    # Only run on Windows
    if os.name == 'nt':
        try: 
            # If target_widget is passed, use it. 
            # This handles both 'self' (from Main) and 'window' (from Popup)
            hwnd = target_widget.winId().__int__()
            
            value = ctypes.c_int(1 if is_dark_mode else 0) 
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20

            try:
                ctypes.windll.dwmapi.DwmSetWindowAttribute(
                    hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, 
                    ctypes.byref(value), ctypes.sizeof(value)
                )
            except Exception:
                DWMWA_USE_IMMERSIVE_DARK_MODE_OLD = 19
                ctypes.windll.dwmapi.DwmSetWindowAttribute(
                    hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE_OLD, 
                    ctypes.byref(value), ctypes.sizeof(value)
                )
        except Exception as e:
            print(f"Could not change window theme: {e}")