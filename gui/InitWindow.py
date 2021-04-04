from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread

import sys

# from manager import *
# from MeetingWindow import MeetingWindow
from multiprocessing import Manager
from gui.MeetingWindow import MeetingWindow

class CreateMeetingThread(QThread):
    def __init__(self,manager):
        QThread.__init__(self)
        self.manager = manager
    def run(self):
        self.manager.createMeeting()  

#这是初始界面
#界面里选择是创建会议，还是加入会议
class InitWindow(QWidget):
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.manager = Manager()
    win.setCentralWidget(InitWindow(win))
    win.show()
    app.exec_()