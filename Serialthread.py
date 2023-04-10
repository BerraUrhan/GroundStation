# serial_thread.py

import serial
from PyQt6.QtCore import QThread, pyqtSignal

class SerialThread(QThread):
    dataReceived = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.serial = serial.Serial('/dev/tty.usbserial-A50285BI', baudrate=115200, timeout=1)

    def write(self, message):
        self.serial.write(message.encode())

    def run(self):
        with serial.Serial('/dev/tty.usbserial-A50285BI', baudrate=115200, timeout=1) as ser:
            print("Connected to", ser.name)

            # Write data to the serial port
            message = "Hello, worlddddddddddd\ryeeeeeeeeeee!"
            ser.write(message.encode())

            while True:
                # decode bytes to string and remove trailing whitespace
                data = ser.readline().decode().strip()
                if data.endswith('#'):
                    print("veri geldi")
                    # remove '#' character from data
                    # data = data[:-1]
                    self.dataReceived.emit(data)
