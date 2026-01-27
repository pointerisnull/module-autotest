from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap

class TextBox(QLabel):
    def __init__(self, text="", color="lightgray"):
        super().__init__(text)
        self.init_UI(color)

    def init_UI(self, color):
        # Center the text within the label's geometry
        self.setAlignment(Qt.AlignCenter)
        
        # This policy tells the layout to expand as much as possible
        self.setSizePolicy(
            self.sizePolicy().Expanding, 
            self.sizePolicy().Expanding
        )

    def set_style(self, font_size=12, bg="white", border=2):
        # Adding a border/background so you can see the geometry change
        self.setStyleSheet(f"""
            border: {border}px solid black;
            background-color: {bg};
            font-size: {font_size}px;
        """)

class ContainerWithBackground(QWidget):
    def __init__(self, image_path, scale_factor=0.5, parent=None):
        super().__init__(parent)
        # Allows themes to work
        self.setAttribute(Qt.WA_StyledBackground, False)

        self.image_path = image_path
        self.pixmap = QPixmap(self.image_path)
        self.scale_factor = scale_factor # 0.5 for 50% size

    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Calculate the new target dimensions based on the scale factor
        new_width = int(self.width() * self.scale_factor)
        new_height = int(self.height() * self.scale_factor)
        
        # Scale the pixmap to these dimensions
        # Qt.KeepAspectRatio ensures the image doesn't look stretched
        scaled_pixmap = self.pixmap.scaled(
            new_width, 
            new_height, 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        
        # Calculate coordinates to keep it perfectly centered
        x = (self.width() - scaled_pixmap.width()) // 2
        y = (self.height() - scaled_pixmap.height()) // 2
        
        painter.drawPixmap(x, y, scaled_pixmap)
        super().paintEvent(event)