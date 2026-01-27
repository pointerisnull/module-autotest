from PyQt5.QtWidgets import *
from gui.Window import *

import sys

if __name__ == "__main__":
    # sys.argv - used to process command line arguments when program is run
    app = QApplication(sys.argv)
    window = MainWindow("HMS Module Autotester")
    window.show()

    sys.exit(app.exec_())