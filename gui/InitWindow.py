from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread

import sys

from manager import *
from MeetingWindow import MeetingWindow
from StatusBarWindow import *


# from multiprocessing import Manager
# from gui.MeetingWindow import MeetingWindow

# 这是初始界面
# 界面里选择是创建会议，还是加入会议
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
        statusBarWindow = StatusBarWindow()
        statusBarWindow.show()
        self.mainWindow.childWindows['statusBarWindow'] = statusBarWindow
        socket_server = SocketServer()

        def socket_server_start():
            gestureListener = GestureListener(statusBarWindow)
            socket_server.runServer(gestureListener)

        self.mainWindow.closeEvents.append(socket_server.terminateServer)
        thread = threading.Thread(target=socket_server_start)
        thread.start()
        self.mainWindow.setCentralWidget(MeetingWindow(self.mainWindow))
        self.mainWindow.setHidden(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.manager = Manager()
    win.setCentralWidget(InitWindow(win))
    win.show()
    app.exec_()
