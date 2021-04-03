
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *

import os
import sys

# 在引入父目录的模块之前加上如下代码：
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from manager import *

# 数据可视化界面
class DataViewWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        tabWidget = QTabWidget()
        self.tabWidget = tabWidget

        series0 = QLineSeries()
        series1 = QLineSeries()
        self.series0 = series0
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
        series.setName("Batman")
        pen = QPen(0x059605)
        pen.setWidth(3)
        series.setPen(pen)

        gradient = QLinearGradient(QPointF(0,0),QPointF(0,1))
        gradient.setColorAt(0.0, QColor(0x3cc63c))
        gradient.setColorAt(1.0, QColor(0x26f626))
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        series.setBrush(gradient)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Simple areachart example")
        chart.createDefaultAxes()
        chart.axes(Qt.Horizontal)[0].setRange(0, 20)
        chart.axes(Qt.Vertical)[0].setRange(0, 10)

        chartWidget = QWidget()
        chartView = QChartView(chart)
        chartView.setGeometry(0,0,100,100)
        chartView.setRenderHint(QPainter.Antialiasing)

        tabWidget.addTab(chartView,"batman")

        tabWidget.setTabPosition(QTabWidget.West)
        tabWidget.setTabShape(QTabWidget.Triangular)
        layout = QVBoxLayout(self)
        layout.addWidget(tabWidget)
        self.setLayout(layout)

# 状态显示条
class StatusBar(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumWidth(100)

        # 设置这个标志可使窗口总是显示在前台
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setWindowOpacity(0.5)

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        leftLabel = QLabel()
        leftPixmap = QPixmap("gui/picture/left.png")
        leftLabel.setPixmap(leftPixmap)
        layout.addWidget(leftLabel, 1)
        rightPixmap = QPixmap("gui/picture/right.png")
        rightLabel = QLabel()
        rightLabel.setPixmap(rightPixmap)
        layout.addWidget(rightLabel, 1)

        clockLabel = QLabel()
        clockPixmap = QPixmap("gui/picture/clock_rotate.png")
        clockLabel.setPixmap(clockPixmap)
        layout.addWidget(clockLabel, 1)

# 会议界面
class MeetingWindow(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self)
        self.mainWindow = mainWindow

        layout = QHBoxLayout(self)
        vLayout1 = QVBoxLayout()
        vLayout2 = QVBoxLayout()
        layout.addLayout(vLayout1,3)
        layout.addLayout(vLayout2,1)
        self.setLayout(layout)
        vLayout1.addWidget(QLabel("aaa"))
        vLayout2.addWidget(QLabel("list"))
        dataViewButton = QPushButton("数据视图")
        dataViewButton.clicked.connect(self.toDataView)
        vLayout2.addWidget(dataViewButton)
        vLayout2.addWidget(QPushButton("quit"))

        hLayout1 = QHBoxLayout()
        vLayout1.addLayout(hLayout1)
        hLayout1.addWidget(QPushButton("开启手势识别"))
        hLayout1.addWidget(QPushButton("接受远程手势操控"))
        self.statusBar = StatusBar()
        self.statusBar.show()

    def toDataView(self):
        self.mainWindow.setCentralWidget(DataViewWindow())





class CreateMeetingThread(QThread):
    def __init__(self,manager):
        QThread.__init__(self)
        self.manager = manager
    def run(self):
        self.manager.createMeeting()  

#这是初始界面
#界面里选择是创建会议，还是加入会议
class InitWidget(QWidget):
    def __init__(self, mainWindow):
        QWidget.__init__(self)
        self.mainWindow = mainWindow

        layout = QVBoxLayout()
        createButton = QPushButton("创建会议")
        createButton.clicked.connect(self.createMeeting)
        layout.addWidget(createButton)

        joinButton = QPushButton("加入会议")
        joinButton.clicked.connect(self.joinMeeting)
        hLayout = QHBoxLayout()
        lineEdit = QLineEdit()
        self.lineEdit = lineEdit
        hLayout.addWidget(lineEdit)
        hLayout.addWidget(joinButton)

        layout.addLayout(hLayout)
        
        self.setLayout(layout)
    
    def joinMeeting(self):
        self.mainWindow.manager.joinMeeting(self.lineEdit.text())
        self.mainWindow.setCentralWidget(MeetingWindow(self.mainWindow))
    def createMeeting(self):
        self.thread = CreateMeetingThread(self.mainWindow.manager)
        self.thread.start()
        self.mainWindow.setCentralWidget(MeetingWindow(self.mainWindow))

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(600,500)
        self.setMinimumSize(600,500)
        self.manager = Manager()
        initWidget = InitWidget(self)
        self.setCentralWidget(initWidget)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()