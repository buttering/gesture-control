from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

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

        leftLabel = QLabel()
        self.leftLabel = leftLabel
        leftPixmap = QPixmap("gui/picture/左移.png")
        leftLabel.setPixmap(leftPixmap)
        layout.addWidget(leftLabel, 1)
        rightPixmap = QPixmap("gui/picture/右移.png")
        rightLabel = QLabel()
        self.rightLabel = rightLabel
        rightLabel.setPixmap(rightPixmap)
        layout.addWidget(rightLabel, 1)

        clockLabel = QLabel()
        self.clockLabel = clockLabel
        clockPixmap = QPixmap("gui/picture/顺时针旋转.png")
        clockLabel.setPixmap(clockPixmap)
        layout.addWidget(clockLabel, 1)

        anticlockLabel = QLabel()
        self.anticlockLabel = anticlockLabel
        anticlockPixmap = QPixmap("gui/picture/逆时针旋转.png")
        anticlockLabel.setPixmap(anticlockPixmap)
        layout.addWidget(anticlockLabel)

        graspLabel = QLabel()
        self.graspLabel = graspLabel
        graspPixmap = QPixmap("gui/picture/抓取.png")
        graspLabel.setPixmap(graspPixmap)
        layout.addWidget(graspLabel)

        zoominLabel = QLabel()
        self.zoominlabel = zoominLabel
        zoominPixmap = QPixmap("gui/picture/放大.png")
        zoominLabel.setPixmap(zoominPixmap)
        layout.addWidget(zoominLabel)

        zoomoutLabel = QLabel()
        self.zoomoutLabel = zoomoutLabel
        zoomoutPixmap = QPixmap("gui/picture/缩小.png")
        zoomoutLabel.setPixmap(zoomoutPixmap)
        layout.addWidget(zoomoutLabel)

    
class GestureListener(object):
    def __init__(self, statusBarWindow):
        self.statusBarWindow = statusBarWindow
        self.pixmap = []
        self.pixmap.append(QPixmap("gui/picture/顺时针旋转1.png"))
        self.pixmap.append(QPixmap("gui/picture/顺时针旋转.png"))
        self.i = 0
    
    def gestureChanged(self, gesturename):
        print('gestureChanged',gesturename)
        self.statusBarWindow.clockLabel.setPixmap(self.pixmap[self.i])
        self.i = (self.i + 1) % 2

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




