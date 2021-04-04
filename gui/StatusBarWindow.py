from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from server.socketServer import *
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

if __name__ == '__main__':
    def socket_server_start():
        socket_server = socketServer()
        socket_server.runServer(sc.IP, sc.PORT)
    thread = threading.Thread(target=socket_server_start)
    thread.start()
    app = QApplication(sys.argv)
    win = StatusBarWindow()
    win.show()
    app.exec_()




