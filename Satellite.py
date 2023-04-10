from PyQt6.QtCore import  Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout

class Satellite(QLabel):
    def __init__(self, value):
        super().__init__()

        self.setFixedSize(150, 150)

        self.setStyleSheet("""
                   background-color: #000; 
                   color: white;
                   font-weight: bold;
                   padding: 2px;
                   border-radius: 10px;
                   border: 1.5px solid rgba(120, 54, 31, 0.7);
                """)


        self.sat_label = QLabel()
        self.label2 = QLabel()
        self.sat_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont()
        font.setPointSize(30)
        self.sat_label.setFixedSize(120, 50)
        self.sat_label.setFont(font)
        self.sat_label.setStyleSheet("""
            color: white;
            background-color: #000; 
            border: 2px solid #000;
            font-weight: bold;
        """)

        font = QFont()
        font.setPointSize(18)
        self.label2.setFont(font)
        self.label2.setText("UYDU\nSTATÜSÜ")
        self.label2.setStyleSheet("""
            color: white;
            background-color: #000; 
            border: 2px solid #000;
            font-weight: bold;
        """)
        self.label2.setFixedSize(120, 60)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.sat_label)
        self.setLayout(vbox2)
        self.sat_label.setText(value)

    def update_status(self, value):
        data = str(int(value))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return self.sat_label.setText(data)