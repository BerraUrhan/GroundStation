from PyQt6.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import matplotlib.font_manager as fm
import numpy as np


class Chart(QMainWindow):
    def __init__(self, rowNumber, xValue, chartColor, title, startValue):
        super().__init__()
        self.xAxisValue = xValue
        self.row = rowNumber
        self.color = chartColor
        self.title = title
        self.dataList = []
        self.setWindowTitle("Real-time Chart")
        self.setGeometry(100, 100, 800, 600)

        # Create the figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)

        # Initialize the plot
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Value")
        self.ax.grid(color='gray', linewidth=0.4)  # Set the grid color to white and linewidth to 0.5
        self.ax.set_title(self.title, fontsize=12)
        self.ax.set_facecolor('#353535')  # change the background color of the chart

        # ------------ make the chart more aesthetic --------------------

        # Change font size of x-axis label
        x_label_font = fm.FontProperties(size=10)
        self.ax.set_xlabel("Zaman (s)", fontproperties=x_label_font)

        # Change font size of y-axis label
        y_label_font = fm.FontProperties(size=10)
        self.ax.set_ylabel(self.xAxisValue, fontproperties=y_label_font)

        # Change font size of x-axis tick labels
        x_tick_font = fm.FontProperties(size=10)
        for tick in self.ax.get_xticklabels():
            tick.set_fontproperties(x_tick_font)

        # Change font size of y-axis tick labels
        y_tick_font = fm.FontProperties(size=10)
        for tick in self.ax.get_yticklabels():
            tick.set_fontproperties(y_tick_font)
        # --------------------------------------------------------------

        # Make the gap between the values shown on the y-axis '10
        # TODO: multiplelocator'ı dynamic olarak güncelle
        #self.ax.yaxis.set_major_locator(ticker.MultipleLocator(150))

        # change the line color and width
        self.line, = self.ax.plot([], [], self.color, linewidth=2)
        self.ax.set_ylim([0, 1000])  # set y-axis limits #TODO: max limit 800 olmak zorunda değil bunu değiştir

        # draw the initial plot
        self.canvas.draw()

    def update_plot(self, new_data, blist):

        # Read the next value from the CSV file and update the plot
        try:

            value = float(new_data.strip())
            blist.append(value)
            self.line.set_xdata(range(len(self.line.get_ydata()) + 1))
            self.line.set_ydata(list(self.line.get_ydata()) + [value])
            # self.line.set_xdata(range(len(self.dataList)))
            # self.line.set_ydata(self.dataList)

            # y_min = min(self.dataList) - 50 if min(self.dataList) > 50 else 0
            # y_max = max(self.dataList) + 50
            #average =
            # TODO: optimizasyon
            if 0 < value < 10:
                y_min = min(self.line.get_ydata()) - 1 if min(self.line.get_ydata()) > 5 else 0
                y_max = max(self.line.get_ydata()) + 1
            else:
                y_min = min(self.line.get_ydata()) - 30 if min(self.line.get_ydata()) > 30 else 0
                y_max = max(self.line.get_ydata()) + 30
            self.ax.set_ylim(y_min, y_max)

            self.ax.relim()
            self.ax.autoscale_view()

            # Fill the area below the curve with a green color
            # lower_curve = [0] * len(self.dataList)
            # self.ax.fill_between(range(len(self.dataList)), self.dataList, y2=lower_curve, color=self.color, alpha=0.1)
            lower_curve = [0] * len(self.line.get_ydata())
            self.ax.fill_between(range(len(self.line.get_ydata())), self.line.get_ydata(), y2=lower_curve,
                                 color=self.color, alpha=0.1)

            self.canvas.draw()

        except Exception as e:
            print(f"Error updating plot: {e}")

