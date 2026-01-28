from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

import os
import ctypes

from gui.Elements import *
from gui.Themes import *
from gui.Options import *
from gui import Popups as popup
from core.ConfigHandler import ConfigHandler
from common import constants

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
        
        self.dark_mode = False
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
        run_menu = menu_bar.addMenu("Run")
        help_menu = menu_bar.addMenu("Help")

        # The '&' allows for Alt+Key shortcuts
        new_config = QAction("&New Configuration", self)
        new_config.setShortcut("Ctrl+N")
        new_config.triggered.connect(self.new_config)
        
        open_config = QAction("&Open Configuration", self)
        open_config.setShortcut("Ctrl+O")
        open_config.triggered.connect(self.set_config)
        
        hardware_config = QAction("&Hardware Configuration", self)
        hardware_config.triggered.connect(lambda: self.popup.hardware_config(self, self.config))
        hardware_config.setShortcut("Ctrl+H")
        
        crimson_config = QAction("Configure Crimson", self)
        crimson_config.triggered.connect(lambda: self.popup.crimson_config(self, self.config))       
        
        style_config = QAction("&Change Style", self)
        style_config.setShortcut("Ctrl+Shift+D")
        style_config.triggered.connect(self.change_style)       

        exit_action = QAction("&Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        about_action = QAction("&About", self)
        about_action.setShortcut("Ctrl+A")
        about_action.triggered.connect(lambda: self.popup.about(self, "About", "HMS Autotester version 0.0.0"))

        run_action = QAction("&Run Hardware Config", self)
        run_action.setShortcut("F5")
        # Placeholder
        run_action.triggered.connect(lambda: self.popup.confirm_action(self, "Running Test", "Would you like to test the current hardware configuration?"))

        # Add options to menues
        file_menu.addAction(new_config)
        file_menu.addAction(open_config)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        edit_menu.addAction(hardware_config)
        
        view_menu.addAction(crimson_config)
        view_menu.addSeparator()
        view_menu.addAction(style_config)
        
        run_menu.addAction(run_action)

        help_menu.addAction(about_action)

    # Called to init / refresh the main screen
    def init_UI(self):

        # Clear the Startup Screen
        #self.main_widget = QWidget()
        self.main_widget = ContainerWithBackground("./assets/hms_logo.png") 
        self.setCentralWidget(self.main_widget)

        # Main Layout (Horizontal Split), with about a 1:3 ratio
        self.main_layout = QHBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(15)

        # Left: IO List
        self.left_panel_layout = QVBoxLayout()

        # Header
        io_label = QLabel("IO Pins")
        self.left_panel_layout.addWidget(io_label)

        self.io_list = QListWidget()
        self.left_panel_layout.addWidget(self.io_list)
        self.main_layout.addLayout(self.left_panel_layout, 1)

        # Right: Options
        self.right_panel_layout = QVBoxLayout()

        # Header
        self.options_title = QLabel("Module Options")
        self.right_panel_layout.addWidget(self.options_title)
        self.options_stack = QStackedWidget()
        self.right_panel_layout.addWidget(self.options_stack)

        # Apply Button
        self.apply_btn = QPushButton("Apply Changes")
        self.apply_btn.setMinimumHeight(40)
        # self.apply_btn.clicked.connect(self.save_changes) # TODO
        self.right_panel_layout.addWidget(self.apply_btn)
        self.main_layout.addLayout(self.right_panel_layout, 3)

        # Finalization
        self.populate_io()

        # Link list selection to the stack widget
        self.io_list.currentRowChanged.connect(self.display_options_page)

        # Select first item by default
        if self.io_list.count() > 0:
            self.io_list.setCurrentRow(0)

    # TEMP: 8DI/8DO IO configuration
    def populate_io(self):
        for i in range(1, 9):
            io_tab = DigitalIn(f"DI_{i}")
            self.io_list.addItem(f"DI_{i}")
            self.options_stack.addWidget(io_tab.get_contents())
        for i in range(1, 9):
            io_tab = DigitalOut(f"DO_{i}")
            self.io_list.addItem(f"DO_{i}")
            self.options_stack.addWidget(io_tab.get_contents())
        

    # Testing options for each IO Pin
    def display_options_page(self, index):
        # Switches the right panel based on the left list selection.
        if index < 0: return

        # Update Title
        current_item = self.io_list.item(index)
        if current_item:
            self.options_title.setText(f"Options: {current_item.text()}")

        # Switch Page
        self.options_stack.setCurrentIndex(index)

    # Create new configuration
    def new_config(self):
        self.popup.new_file(self, "New Configuration", self.config)
        if self.config.has_changed:
            self.init_UI()

    # Select configuration
    def set_config(self):
        self.popup.open_config(self, self.config)
        if self.config.has_changed:
            self.init_UI()

    # Light | Dark mode
    def change_style(self):
        if self.dark_mode:
            self.setStyleSheet(LIGHT_MODE)
        else:
            self.setStyleSheet(DARK_MODE)
        self.dark_mode = not self.dark_mode
        self.popup.change_style()
        
        update_titlebar(self, self.dark_mode)

# Update the windows border theme
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