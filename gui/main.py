from PyQt5.QtWidgets import *
import sys
from interface import Interface

class JoinWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)
        commitButton = QPushButton("确认")
        commitButton.clicked.connect(self.commit)
        layout.addWidget(commitButton)
        self.setLayout(layout)
    
    def commit(self):
        ip = self.lineEdit.text()

class CreateWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        

#这是初始界面
#界面里选择是创建会议，还是加入会议
class InitWidget(QWidget):
    def __init__(self,joinButtonClicked):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("创建会议"))
        joinButton = QPushButton("加入会议")
        layout.addWidget(joinButton)
        joinButton.clicked.connect(joinButtonClicked)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    inter = Interface()
    def __init__(self):
        QMainWindow.__init__(self)
        initWidget = InitWidget(self.toJoinWidget)
        joinWidget = JoinWidget()
        self.setCentralWidget(initWidget)
    
    def toJoinWidget(self):
        self.setCentralWidget(JoinWidget())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()