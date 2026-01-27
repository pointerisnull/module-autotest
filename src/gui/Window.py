from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

from gui.Elements import *
from core.ConfigHandler import ConfigHandler
from common import constants
from gui import Popups as popup

# PyQt5 Documentation:
# https://www.riverbankcomputing.com/static/Docs/PyQt5/

class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setGeometry(0, 0, constants.DEFAULT_WIDTH, constants.DEFAULT_HEIGHT)
        self.setWindowTitle(title)
        self.container = QWidget()
        self.setCentralWidget(self.container)
        self.startup_screen = QVBoxLayout(self.container)

        self.intro = TextBox("To start, select or create a new testing configuration.")
        self.startup_screen.addWidget(self.intro)

        self.init_menu_bar()

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


if __name__ == "__main__":
    # sys.argv - used to process command line arguments when program is run
    app = QApplication(sys.argv)
    window = MainWindow("HMS Module Autotester")
    window.show()

    sys.exit(app.exec_())