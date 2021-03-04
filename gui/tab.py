from PyQt5.QtWidgets import *

import sys

class TabWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1300,800)
        tabWidget = QTabWidget(self)
        self.tabWidget = tabWidget
        tabWidget.addTab(QTextEdit("hh"),"1")
        tabWidget.addTab(QTextEdit("fff"),"2")
        self.setCentralWidget(tabWidget)

app = QApplication(sys.argv)
win = TabWindow()
win.show()
app.exec_()