from PyQt6.QtCore import  Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout


class ErrorCode(QLabel):
    def __init__(self, value):
        super().__init__()

        self.setStyleSheet("""
                   background-color: #000; 
                   color: white;
                   font-weight: bold;
                   padding: 2px;
                   border-radius: 10px;
                   border: 1.5px solid rgba(120, 54, 31, 0.7);
               """)
        # Create a QHBoxLayout to hold the color sections
        hbox = QHBoxLayout()
        self.label = QLabel()
        self.label2 = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont()
        font.setPointSize(16)
        font2 = QFont()
        font2.setPointSize(8)
        self.label.setFont(font)
        self.label2.setFont(font2)
        self.label.setText("HATA KODU")
        self.label.setStyleSheet("""
                        color: white;
                        background-color: #000; 
                        border: 2px solid #000;
                    """)
        self.label2.setStyleSheet("""
                        color: white;
                        background-color: #000; 
                        border: 2px solid #000;
                        font-weight: normal;
                        border-radius: 5px;
                        padding: 0.5px;
                    """)
        self.label.setFixedSize(120, 60)

        self.hbox = QHBoxLayout()

        # Iterate over the digits in the number and create a QLabel for each section
        for digit in str(value):
            color_label = QLabel()

            color_label.setStyleSheet("""
                                background-color: red;
                                border-radius: 5px;
                                border: 0.2px solid white;
                            """)

            # Set the fixed size of the label to 20x20
            color_label.setFixedSize(15, 18)

            # Set the background color of the label based on the digit value
            if digit == '1':
                color_label.setStyleSheet("background-color: red;")
            else:
                color_label.setStyleSheet("background-color: green;")

            # Add the label to the QVBoxLayout
            self.hbox.addWidget(color_label)

        # Set the layout of the label to the QBoxLayout we just created
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(self.hbox)
        vbox.addWidget(self.label2)
        self.setLayout(vbox)

    def update_error(self, value):
        # Iterate over the digits in the number and update the QLabel for each section
        for i, digit in enumerate(str(value)):
            color_label = self.hbox.itemAt(i).widget()
            if digit == '1':
                color_label.setStyleSheet("""
                    background-color: red;
                    border-radius: 5px;
                    border: 0.2px solid white;
                """)
            else:
                color_label.setStyleSheet("""
                    background-color: green;
                    border-radius: 5px;
                    border: 0.2px solid white;
                """)

            """if digit == '1' and i == 0:
                text += "taşıyıcı iniş hızı saptı"
            if digit == '1' and i == 1:
                text += "\ngörev yükü iniş hızı saptı"
            if digit == '1' and i == 2:
                text += "\ntaşıyıcıdan basıncı alınamadı"
            if digit == '1' and i == 3:
                text += "\ngörev yükü konumu alınamadı"
            if digit == '1' and i == 4:
                text += "\nayrılmama durumu"
                self.label2.setText(text)
"""


