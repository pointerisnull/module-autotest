DARK_MODE = """
    QMainWindow {
        background-color: #292929;
    }
    
    QWidget {
        /*background-color: #292929;*/
        background-color: rgba(41, 41, 41, 100); 
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

    QDialog {
        background-color: #1E1E1E;
    }


    QComboBox {
        background-color: #333333;
        border: 1px solid #444444;
        border-radius: 8px;
        padding: 5px;
        color: #E0E0E0;
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px;
        border-left: none;
        border-top-right-radius: 8px; 
        border-bottom-right-radius: 8px;
    }

    QComboBox::down-arrow {
        image: none;  /* Optional: replace with custom arrow or keep default */
        border-top: 5px solid #E0E0E0; /* Simple CSS Arrow */
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        margin-top: 2px;
    }

    QComboBox QAbstractItemView {
        background-color: #2D2D2D;
        color: #E0E0E0;
        border: 1px solid #0078D7;
        selection-background-color: #0078D7; /* Blue background for selected item */
        selection-color: #FFFFFF; /* White text for selected item */
        outline: none;
    }

    QDialog QLabel {
        color: #E0E0E0;
        font-size: 16px;
    }

    QScrollBar:vertical {
        border: none;
        background: #2D2D2D;
        width: 10px;
        margin: 0px;
    }

    QScrollBar::handle:vertical {
        background: #444444;
        min-height: 20px;
        border-radius: 5px;
    }
    QListWidget {
        /*background-color: #333333;  Dark background */
        background-color: rgba(51, 51, 51, 100); 
        border: 1px solid #444444;
        color: #E0E0E0;
        outline: 0; /* Removes the dotted focus line */
    }
    
    QListWidget::item:selected {
        background-color: #0078D7; /* Your Blue Highlight */
        color: white;
    }
    
    QWidget:disabled {
        color: #606060; 
    }

    QLineEdit:disabled, QComboBox:disabled, QPushButton:disabled, QListWidget:disabled {
        background-color: #222222;
        color: #606060;
        border: 1px solid #333333;
    }

    QGroupBox {
        color: #E0E0E0; 
        /*background-color: rgba(0, 0, 0, 100);*/ 
    }   

    QGroupBox:disabled {
        color: #606060;
    }

    QFormLayout {
        font-size: 12px;
        margin-top: 20px;
        border: 1px solid #444444;
    }

    QCheckBox {
        color: #E0E0E0;
        selection-color: #D0D0D0;
    }

    QLabel {
        color: #E0E0E0;
    }

"""

LIGHT_MODE = """
    QMainWindow {
        background-color: #F8F9FA;
    }
    
    QWidget {
        /*background-color: #F8F9FA;*/
        background-color: rgba(255, 255, 255, 150)
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

    QDialog {
        background-color: #FDFDFD;
    }

    QComboBox {
        background-color: #FFFFFF;
        border: 1px solid #DCDFE6;
        border-radius: 8px;
        padding: 4px;
        color: #2D3436;
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px;
        border-left: none; 
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
    }

    QComboBox::down-arrow {
        image: none;
        border-top: 5px solid #606266;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        margin-top: 2px;
    }

    QComboBox:on, QComboBox:focus {
        border: 2px solid #409EFF; /* Soft Blue border when active */
    }

    QComboBox QAbstractItemView {
        background-color: #FFFFFF;
        color: #2D3436;
        border: 1px solid #409EFF;
        selection-background-color: #409EFF; /* Soft Blue highlight */
        selection-color: #FFFFFF;
        outline: none;
    }

    QDialog QLabel {
        color: #2D3436;
        font-size: 16px;
    }

    QScrollBar:vertical {
        border: none;
        background: #F0F2F5;
        width: 10px;
    }

    QScrollBar::handle:vertical {
        background: #C0C4CC;
        min-height: 20px;
        border-radius: 5px;
    }
    
    QWidget:disabled {
        color: #B0B0B0;
    }

    QLineEdit:disabled, QComboBox:disabled, QPushButton:disabled {
        background-color: #F7F7F7;
        color: #B0B0B0;
        border: 1px solid #EAEAEA;
    }

    QGroupBox:disabled {
        border: 1px solid #EAEAEA;
        color: #B0B0B0;
    }

    QListWidget {
        background-color: rgba(248, 249, 250, 200)
    }
"""