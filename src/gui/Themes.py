DARK_MODE = """
    QMainWindow {
        background-color: #292929;
    }
    
    QWidget {
        background-color: #292929;
    }

    QLabel {
        color: #E0E0E0;
        background-color: transparent;
    }

    QPushButton {
        background-color: #333333;
        color: #E0E0E0;
        border: 1px solid #444444;
        border-radius: 8px;
        padding: 8px 16px;
    }

    QPushButton:hover {
        background-color: #3D3D3D;
        border: 1px solid #0078D7;
        color: #FFFFFF;
    }

    QPushButton:pressed {
        background-color: #222222;
        border: 1px solid #005A9E;
    }

    QMenuBar {
        background-color: #252526;
        color: #E0E0E0;
        padding: 2px;
        border-bottom: 1px solid #333333;
    }

    QMenuBar::item {
        padding: 6px 12px;
        background-color: transparent;
        border-radius: 4px;
    }

    QMenuBar::item:selected {
        background-color: #3E3E42;
        color: #0078D7;
    }

    QMenu {
        background-color: #252526;
        color: #E0E0E0;
        border: 1px solid #454545;
        border-radius: 6px;
        padding: 4px;
    }

    QMenu::item {
        padding: 6px 30px 6px 25px;
        border-radius: 4px;
    }

    QMenu::item:selected {
        background-color: #0078D7;
        color: #FFFFFF;
    }

    QInputDialog {
        background-color: #292929;
    }

    QLineEdit {
        background-color: #333333;
        color: #E0E0E0;
        border: 1px solid #444444;
        border-radius: 4px;
        padding: 5px;
        selection-background-color: #0078D7;
    }

    QLineEdit:focus {
        border: 1px solid #0078D7;
    }
"""

LIGHT_MODE = """
    QMainWindow {
        background-color: #F8F9FA;
    }
    
    QWidget {
        background-color: #F8F9FA;
    }

    QLabel {
        color: #2D3436;
        background-color: transparent;
    }

    QPushButton {
        background-color: #FFFFFF;
        color: #2D3436;
        border: 1px solid #DCDFE6;
        border-radius: 8px;
        padding: 8px 16px;
    }

    QPushButton:hover {
        background-color: #F2F6FC;
        border: 1px solid #409EFF;
        color: #409EFF;
    }

    QPushButton:pressed {
        background-color: #EBEEF5;
        border: 1px solid #3a8ee6;
    }

    QMenuBar {
        background-color: #F0F0F0;
        color: #2D3436;
        padding: 2px;
        border-bottom: 1px solid #E4E7ED;
    }

    QMenuBar::item {
        padding: 6px 12px;
        background-color: transparent;
        border-radius: 4px;
    }

    QMenuBar::item:selected {
        background-color: #F5F7FA;
        color: #409EFF;
    }

    QMenu {
        background-color: #FFFFFF;
        color: #2D3436;
        border: 1px solid #E4E7ED;
        border-radius: 6px;
        padding: 4px;
    }

    QMenu::item {
        padding: 6px 30px 6px 25px;
        border-radius: 4px;
    }

    QMenu::item:selected {
        background-color: #409EFF;
        color: #FFFFFF;
    }
"""