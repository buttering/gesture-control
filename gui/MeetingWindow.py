from PyQt5.QtWidgets import *


import sys

# from gui.StatusBarWindow import StatusBarWindow
#from gui.DataViewWindow import DataViewWindow
from StatusBarWindow import StatusBarWindow
from DataViewWindow import DataViewWindow

# 会议界面
class MeetingWindow(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self)
        self.mainWindow = mainWindow

        layout = QHBoxLayout(self)
        vLayout1 = QVBoxLayout()
        vLayout2 = QVBoxLayout()
        layout.addLayout(vLayout1,3)
        layout.addLayout(vLayout2,1)
        self.setLayout(layout)
        vLayout1.addWidget(QLabel("aaa"))
        vLayout2.addWidget(QLabel("list"))
        dataViewButton = QPushButton("数据视图")
        dataViewButton.clicked.connect(self.toDataView)
        vLayout2.addWidget(dataViewButton)
        vLayout2.addWidget(QPushButton("quit"))

        hLayout1 = QHBoxLayout()
        vLayout1.addLayout(hLayout1)
        hLayout1.addWidget(QPushButton("开启手势识别"))
        hLayout1.addWidget(QPushButton("接受远程手势操控"))
        self.statusBar = StatusBarWindow()
        self.statusBar.show()

    def toDataView(self):
        self.mainWindow.setCentralWidget(DataViewWindow())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setCentralWidget(MeetingWindow(win))
    win.show()
    app.exec_()
