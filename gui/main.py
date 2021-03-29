
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import os
import sys

# 在引入父目录的模块之前加上如下代码：
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from manager import *

# 状态显示条
class StatusBar(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumWidth(300)

        # 设置这个标志可使窗口总是显示在前台
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        #self.setWindowFlag(Qt.FramelessWindowHint)

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        leftLabel = QLabel()
        leftPixmap = QPixmap("gui/left.png")
        leftLabel.setPixmap(leftPixmap)
        layout.addWidget(leftLabel, 1)
        rightPixmap = QPixmap("gui/right.png")
        rightLabel = QLabel()
        rightLabel.setPixmap(rightPixmap)
        layout.addWidget(rightLabel, 1)

        clockLabel = QLabel()
        clockPixmap = QPixmap("gui/clock_rotate.png")
        clockLabel.setPixmap(clockPixmap)
        layout.addWidget(clockLabel, 1)

# 会议界面
class MeetingWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout(self)
        vLayout1 = QVBoxLayout()
        vLayout2 = QVBoxLayout()
        layout.addLayout(vLayout1,3)
        layout.addLayout(vLayout2,1)
        self.setLayout(layout)
        vLayout1.addWidget(QLabel("aaa"))
        vLayout2.addWidget(QLabel("list"))
        vLayout2.addWidget(QLabel("quit"))
        hLayout1 = QHBoxLayout()
        vLayout1.addLayout(hLayout1)
        hLayout1.addWidget(QPushButton())
        hLayout1.addWidget(QPushButton())
        self.statusBar = StatusBar()
        self.statusBar.show()





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
        #self.mainWindow.manager.joinMeeting(self.lineEdit.text())
        self.mainWindow.setCentralWidget(MeetingWindow())
    def createMeeting(self):
        #self.thread = CreateMeetingThread(self.mainWindow.manager)
        #self.thread.start()
        self.mainWindow.setCentralWidget(MeetingWindow())

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