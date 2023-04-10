from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame


class DigitalClock(QLabel):
    def __init__(self, time_string):
        super().__init__()

        # Set the data list
        self.time_string = time_string
        self.setFixedSize(150, 150)

        # Set the style sheet for the widget
        self.setStyleSheet("""
                    background-color: #000;
                    padding: 5px;
                    border-radius: 10px;
                    border: 1.5px solid rgba(120, 54, 31, 0.7);
                """)

        # Create the label to display the clock
        self.clock_label = QLabel()
        self.label = QLabel()
        self.clock_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the font for the label
        font = QFont("Tahoma")
        font.setPointSize(25)
        self.clock_label.setFont(font)

        # Set the font for the label
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setText("SAAT")
        self.label.setStyleSheet("""
            color: white;
            font-size: 30;
            background-color: #000; 
            border: 2px solid #000;
            font-weight: bold;
            """)
        self.label.setFixedSize(120, 40)

        # Set the style of the label using CSS
        self.clock_label.setStyleSheet("""
                background-color: #226;
                color: white;
                font-size: 20;
                border-radius: 10px;
                border: 2px solid #220;
                padding: 1px;
            """)

        # Add the label to the widget
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.clock_label)
        self.setLayout(vbox)
        self.clock_label.setText(time_string)

    def update_clock(self, time_string):
        # Update the clock label
        data = str(time_string.strip().split(" ")[1])
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return self.clock_label.setText(data)



