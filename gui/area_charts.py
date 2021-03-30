from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class DataViewWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        tabWidget = QTabWidget()
        tabWidget = tabWidget

        series0 = QLineSeries()
        self.series0 = series0
        series1 = QLineSeries()
        self.series1 = series1

        series0.append(1, 5)
        series0.append(3, 7)
        series0.append(7, 6)
        series0.append(9, 7)
        series0.append(16, 7)
        series0.append(18, 5)
        series1.append(1, 3)
        series1.append(3, 4)
        series1.append(7, 3)
        series1.append(8, 2)
        series1.append(16, 4)
        series1.append(18, 3)

        series = QAreaSeries(series0, series1)
        series = series
        series.setName("Batman")
        pen = QPen(0x059605)
        pen.setWidth(3)
        series.setPen(pen)

        gradient = QLinearGradient(QPointF(0,0),QPointF(0,1))
        gradient = gradient
        gradient.setColorAt(0.0, QColor(0x3cc63c))
        gradient.setColorAt(1.0, QColor(0x26f626))
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        series.setBrush(gradient)

        chart = QChart()
        chart = chart
        chart.addSeries(series)
        chart.setTitle("Simple areachart example")
        chart.createDefaultAxes()
        chart.axes(Qt.Horizontal)[0].setRange(0, 20)
        chart.axes(Qt.Vertical)[0].setRange(0, 10)

        chartWidget = QWidget()
        chartView = QChartView(chart, chartWidget)
        chartView.setGeometry(0,0,100,100)
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView = chartView

        tabWidget.addTab(chartWidget,"batman")

        tabWidget.setTabPosition(QTabWidget.West)
        tabWidget.setTabShape(QTabWidget.Triangular)
        self.setCentralWidget(tabWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = DataViewWindow()
    widget.show()
    app.exec_()