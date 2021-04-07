from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread, QObject, pyqtSignal

import time

# 在引入父目录的模块之前加上如下代码：
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))

from server.SocketServer import *
import config.socketConfig as sc
import threading

import sys

# 状态显示条
class StatusBarWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumWidth(100)

        # 设置这个标志可使窗口总是显示在前台
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setWindowOpacity(0.9)

        desktop = QApplication.desktop()
        rect = desktop.geometry()
        self.setGeometry(rect.width()-170,40,130,0)

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        pictureNames = [                
                "click",
                "panLeft",
                "panRight",
                "enlarge",
                "narrow",
                "grasp",
                "cwr",
                "ccwr"]
        pixmaps0 = {}
        pixmaps1 = {}
        for name in pictureNames:
            pixmaps0[name] = QPixmap("gui/picture/"+name+'0.png')
            pixmaps1[name] = QPixmap("gui/picture/"+name+'1.png')
        self.pixmaps0 = pixmaps0
        self.pixmaps1 = pixmaps1

        statusLabels = {}
        self.statusLabels = statusLabels
        for name in pictureNames:
            label = QLabel()
            statusLabels[name] = label
            label.setPixmap(pixmaps0[name])
            layout.addWidget(label, 1)
    
class GestureListener(object):
    def __init__(self, statusBarWindow):
        self.statusBarWindow = statusBarWindow
    
    def gestureChanged(self, gesturename):
        print('gestureChanged',gesturename)
        label = self.statusBarWindow.statusLabels[gesturename]
        pixmap = self.statusBarWindow.pixmaps1[gesturename]
        pixmap0 = self.statusBarWindow.pixmaps0[gesturename]
        label.setPixmap(pixmap)

        def delay():
            label0 = label
            pixmap00 = pixmap0
            time.sleep(1)
            label0.setPixmap(pixmap00)
        # Step 6: Start the thread
        self.thread = threading.Thread(target=delay)
        self.thread.start()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = StatusBarWindow()
    def socket_server_start():
        gestureListener = GestureListener(win)
        socket_server = SocketServer()
        # socket_server.runServer(sc.IP, sc.PORT)
        socket_server.runServer(gestureListener)

    thread = threading.Thread(target=socket_server_start)
    thread.start()
    win.show()
    app.exec_()




