
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import sys
import os

# 统一不同工作环境的当前工作目录，统一为项目根目录
current_dir,file_name = os.path.split(os.path.abspath(sys.argv[0]))
print(current_dir)
project_root_dir, dir_name = os.path.split(current_dir)
os.chdir(project_root_dir)

from manager import *
from MeetingWindow import MeetingWindow
from InitWindow import InitWindow

#from multiprocessing import Manager
#from gui.MeetingWindow import MeetingWindow
#from gui.InitWindow import InitWindow



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