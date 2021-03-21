from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import sys

class TopWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    topWindow = TopWindow()
    topWindow.show()
    app.exec_()