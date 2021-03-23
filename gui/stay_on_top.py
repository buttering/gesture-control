from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import sys

class TopWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # 设置这个标志可使窗口总是显示在前台
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    topWindow = TopWindow()
    topWindow.show()
    app.exec_()