import numpy as np
import pyqtgraph as pg
from PyQt6.QtWidgets import QMainWindow


class Gyro(QMainWindow):
    def __init__(self, pitch, roll, yaw):
        super().__init__()

        self.pitch_data = []
        self.roll_data = []
        self.yaw_data = []

        # Set up the graph
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.graphWidget.showGrid(x=True, y=True)

        # Add legend
        self.graphWidget.addLegend()

        # Create the data lines
        self.pitch_line = self.graphWidget.plot(pen=pg.mkPen('r', width=3), symbolBrush=0.1, symbolPen='r', name="Pitch")
        self.roll_line = self.graphWidget.plot(pen=pg.mkPen('g', width=3), symbolBrush=0.1, symbolPen='g', name='Roll')
        self.yaw_line = self.graphWidget.plot(pen=pg.mkPen('b', width=3), symbolBrush=0.1, symbolPen='b', name='Yaw')

        # Update the data lines with the initial values
        self.update_plot(pitch, roll, yaw)

    def update_plot(self, pitch, roll, yaw):
        # Convert the input values to float
        pitch = np.array(pitch).astype(float)
        roll = np.array(roll).astype(float)
        yaw = np.array(yaw).astype(float)

        # Append the new values to the data lists
        self.pitch_data.append(pitch)
        self.roll_data.append(roll)
        self.yaw_data.append(yaw)

        # Update the data lines with all values in the lists
        self.pitch_line.setData(self.pitch_data)
        self.roll_line.setData(self.roll_data)
        self.yaw_line.setData(self.yaw_data)

