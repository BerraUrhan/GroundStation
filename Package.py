from PyQt6.QtCore import  Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QVBoxLayout

class Package(QLabel):
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


        self.package_label = QLabel()
        self.label = QLabel()
        self.package_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont()
        font.setPointSize(30)
        self.package_label.setFixedSize(120, 50)
        self.package_label.setFont(font)
        self.package_label.setStyleSheet("""
            color: white;
            background-color: #000; 
            border: 2px solid #000;
            font-weight: bold;
            """)

        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("PAKET\nNUMARASI")
        self.label.setStyleSheet("""
                color: white;
                background-color: #000; 
                border: 2px solid #000;
            """)
        self.label.setFixedSize(120, 60)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.package_label)
        self.setLayout(vbox)
        self.package_label.setText(value)


    def update_package(self, value):
            data = str(int(value))
            self.setAlignment(Qt.AlignmentFlag.AlignCenter)

            return self.package_label.setText(data)
