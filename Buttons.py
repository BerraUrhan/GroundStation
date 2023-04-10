from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QDialog

from Serialthread import SerialThread
from FTPhandler import  MainWindowFTP


# TODO: QFileDialog - button action - better with callback


class ButtonPanel(QWidget):
    def __init__(self, titles):
        super().__init__()
        try:
            self.serial_thread = SerialThread()
        except Exception:
            pass

        self.buttons_layout = QVBoxLayout()
        self.setLayout(self.buttons_layout)

        self.buttons = []
        for title in titles:
            button = QPushButton(title)
            # button styling
            button.setStyleSheet('''
                QPushButton {
                background-color: #222;
                border-radius: 15px;
                border: 1.5px solid rgba(29, 185, 84, 0.8);
                color: #fff;
                font-family: Arial;
                font-size: 14px;
                font-weight: 300;
                padding: 6px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #8f8f91;
            }
                       ''')
            if title == "Video Yükle":
                button.clicked.connect(self.open_ftp_gui)
            elif title == "Telemetri Akışı":
                button.clicked.connect(self.send_telemetry)
            elif title == "Akışı Durdur":
                button.clicked.connect(self.durdur)
            elif title == "Ayrıl":
                button.clicked.connect(self.ayril)
            elif title == "Kitlen":
                button.clicked.connect(self.kitlen)

            button.setMaximumSize(130, 50)
            button.setMinimumSize(120, 30)
            self.buttons.append(button)
            self.buttons_layout.addWidget(button)

    def open_ftp_gui(self):
        dialog = QDialog()
        ftp_gui = MainWindowFTP(dialog)
        ftp_gui.show()
        dialog.exec()


    @pyqtSlot()
    def send_telemetry(self):
        print("karşim hayırdır")
        message = "!1"
        self.serial_thread.write(message)

    @pyqtSlot()
    def durdur(self):
        message = "!2"
        self.serial_thread.write(message)

    @pyqtSlot()
    def kitlen(self):
        message = "!4"
        self.serial_thread.write(message)

    @pyqtSlot()
    def ayril(self):
        message = "!3"
        self.serial_thread.write(message)


