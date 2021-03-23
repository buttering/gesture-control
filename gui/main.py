
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread

import os
import sys

# 在引入父目录的模块之前加上如下代码：
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from manager import *

class MeetingWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        label = QLabel("已加入会议")
        layout = QVBoxLayout(self)
        layout.addWidget(label)

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
        self.mainWindow.setCentralWidget(MeetingWindow())
    def createMeeting(self):
        self.thread = CreateMeetingThread(self.mainWindow.manager)
        self.thread.start()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(600,500)
        self.manager = Manager()
        initWidget = InitWidget(self)
        self.setCentralWidget(initWidget)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()