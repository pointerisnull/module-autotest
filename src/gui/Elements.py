from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

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