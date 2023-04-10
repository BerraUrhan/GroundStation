from PyQt6.QtCore import  Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout


class TeamNumber(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 120)
        self.setStyleSheet("""
                     background-color: #000; 
                     color: white;
                     font-weight: bold;
                     padding: 5px;
                     border-radius: 10px;
                     border: 2px solid rgba(250, 154, 74, 0.8);
                     """)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Get the current font
        font = self.font()
        # Set the font size
        font.setPointSize(22)
        # Set the new font
        self.setFont(font)
        self.setText(f"Takım Numarası")

    def update_tnumber(self, data):
        self.setText(f"Takım Numarası\n{data}")
