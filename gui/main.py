
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *

import sys

from manager import *
from MeetingWindow import MeetingWindow
from InitWindow import InitWindow




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(600,500)
        self.setMinimumSize(600,500)
        self.manager = Manager()
        initWindow = InitWindow(self)
        self.setCentralWidget(initWindow)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()