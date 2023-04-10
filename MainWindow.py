import time

from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, QLabel
import serial

from ErrorCode import ErrorCode
from Gyro import Gyro
from Clock import DigitalClock
from Chart import Chart
from Buttons import ButtonPanel
from Package import Package
from Satellite import Satellite
from Serialthread import SerialThread
from TeamNumber import TeamNumber
from telemtryLine import TelemetryLine
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ground Station")
        self.setGeometry(100, 100, 1800, 900)
        self.setStyleSheet("background-color: #2D2D2D")

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # ---------------- CREATING GENERAL LAYOUTS ----------------

        # create a main layout for main widget
        self.main_layout = QVBoxLayout(self.main_widget)

        # create upper and lower half layouts
        self.upper_half = QGridLayout()
        self.lower_half = QHBoxLayout()

        # create LAYOUTS for buttons, teamNum-logo, left_bottom_corner, 4_box layout
        self.buttons_layout = QVBoxLayout()
        self.logo_layout = QGridLayout()
        self.l_bottom_corner_layout = QHBoxLayout()
        self.four_box_layout = QGridLayout()

        # --------------------------- LOGO ----------------------------
        # Create a QPixmap from the WebP image file

        pixmap = QPixmap("icon.jpg")
        # Scale the image to the desired size
        scaled_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)

        # Create a QLabel to hold the QPixmap
        self.logo_label = QLabel()
        self.logo_label.setPixmap(scaled_pixmap)

        # ------------------------BUTTONS------------------------------------


        # create buttons
        # TODO: bunları class'a yaz
        titles = ['Telemetri Akışı', 'Akışı Durdur', 'Video Yükle', 'Ayrıl', 'Kitlen']
        button_panel = ButtonPanel(titles)
        self.buttons_layout.addWidget(button_panel)

        # ------------------------CREATE WİDGETS-----------------------------

        self.package_num = Package("0")
        self.satellite_status = Satellite("0")
        self.error_code = ErrorCode("01010")
        self.team_number = TeamNumber()
        self.clock = DigitalClock("0:0:0")
        self.gyroChart = Gyro("0","0","0")

        self.chart1 = Chart(4, "Basınç (Pa)", '#DB3A1A', "Basınç 1", 0)  # 1 - basınç 1
        self.chart2 = Chart(5, "Basınç (Pa)", '#DB3A1A', "Basınç 2", 0)  # 2 - basınç 2
        self.chart3 = Chart(4, "Yükseklik (m)", '#1DB954', "Yükseklik 1", 0)  # 3 - yükseklik 1
        self.chart4 = Chart(4, "Yükseklik (m)", '#1DB954', "Yükseklik 2", 0)  # 4 - yükseklik 2

        # upper half 2nd row charts
        self.chart5 = Chart(4, "İrtifa Fark (m)", '#1A3ADB', "İrtifa Farkı", 0)  # 5 - irtifa farkı
        self.chart6 = Chart(0, "Hız (m/s)", '#7F1ADB', "İniş Hızı", 0)  # 6 - iniş hızı
        self.chart7 = Chart(4, "Sıcaklık (°C)", '#F69B2D', "Sıcaklık", 0)  # 7 - sicaklik
        self.chart8 = Chart(4, "Pil Gerilimi (V)", '#2EB4EA', "Pil Gerilimi", 0)  # 8 - pil gerilimi

        self.basinc1List = []
        self.basinc2List = []
        self.basinc3List = []
        self.basinc4List = []
        self.basinc5List = []
        self.basinc6List = []
        self.basinc7List = []
        self.basinc8List = []
        # -----------------------------------------------------------
        self.addLayout()
        # create a serial thread to read data from the serial port
        try:
            self.serial_thread = SerialThread()
            self.serial_thread.dataReceived.connect(self.on_data_received)
            self.serial_thread.start()
        #TODO: bişiler
        except Exception:
            pass

    def on_data_received(self, data):
        data_list = data.split(',')

        # VARIABLES
        paket_numarasi = data_list[0]
        uydu_status = data_list[1]
        hata_kod = data_list[2]
        gonderme_saati = data_list[3]
        basinc1 = data_list[4]
        basinc2 = data_list[5]
        yukseklik1 = data_list[6]
        yukseklik2 = data_list[7]
        irtifa_fark = data_list[8]
        inis_hizi = data_list[9]
        sicaklik = data_list[10]
        pil_gerilimi = data_list[11]
        gps_latitude = data_list[12]
        gps_longtitude = data_list[13]
        gps_altitude = data_list[14]
        pitch = data_list[15]
        roll = data_list[16]
        yaw = data_list[17]
        takim_numarasi = data_list[18]

        self.package_num.update_package(paket_numarasi)
        self.satellite_status.update_status(uydu_status)
        self.team_number.update_tnumber(takim_numarasi)
        self.clock.update_clock(gonderme_saati)
        self.gyroChart.update_plot(pitch, roll, yaw)
        #self.error_code.update_error(hata_kod)

        self.chart1.update_plot(basinc1,self.basinc1List)
        self.chart2.update_plot(basinc2,self.basinc1List)
        self.chart3.update_plot(yukseklik1,self.basinc1List)
        self.chart4.update_plot(yukseklik2,self.basinc1List)

        # upper half 2nd row charts
        self.chart5.update_plot(irtifa_fark,self.basinc1List)
        self.chart6.update_plot(inis_hizi,self.basinc1List)
        self.chart7.update_plot(sicaklik,self.basinc1List)
        self.chart8.update_plot(pil_gerilimi,self.basinc1List)

        self.clock.update_clock(gonderme_saati)
        print(data_list)
        self.addLayout()

    def addLayout(self):
        self.four_box_layout.addWidget(self.package_num, 0, 0)
        self.four_box_layout.addWidget(self.satellite_status, 0, 1)
        self.four_box_layout.addWidget(self.error_code, 1, 0)
        self.four_box_layout.addWidget(self.clock, 1, 1)

        self.logo_layout.addWidget(self.team_number, 0, 0)
        self.logo_layout.addWidget(self.logo_label, 1, 0)

        #self.l_bottom_corner_layout.addWidget(QLabel("LİVECAM"))
        #self.l_bottom_corner_layout.addWidget(self.camera_widget._camera_viewfinder)
        #self.l_bottom_corner_layout.addWidget(QLabel("MAP"))
        self.l_bottom_corner_layout.addWidget(self.gyroChart)

        self.lower_half.addLayout(self.l_bottom_corner_layout)
        self.lower_half.addLayout(self.four_box_layout)
        self.lower_half.addLayout(self.buttons_layout)
        self.lower_half.addLayout(self.logo_layout)

        # add chart widgets to upper half
        self.upper_half.addWidget(self.chart1, 1, 0)
        self.upper_half.addWidget(self.chart2, 1, 1)
        self.upper_half.addWidget(self.chart3, 1, 2)
        self.upper_half.addWidget(self.chart4, 1, 3)

        self.upper_half.addWidget(self.chart5, 2, 0)
        self.upper_half.addWidget(self.chart6, 2, 1)
        self.upper_half.addWidget(self.chart7, 2, 2)
        self.upper_half.addWidget(self.chart8, 2, 3)

        self.lower_half.addLayout(self.four_box_layout)

        self.main_layout.addLayout(self.upper_half)
        self.main_layout.addLayout(self.lower_half)

        # set the main layout to the main widget
        self.main_widget.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
