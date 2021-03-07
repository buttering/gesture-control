from PyQt5.QtWidgets import *
import sys
from interface import Interface

class JoinWidget(QWidget):
    def __init__(self,inter):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)
        commitButton = QPushButton("确认")
        commitButton.clicked.connect(self.commit)
        layout.addWidget(commitButton)
        self.setLayout(layout)
        self.inter = inter
    
    def commit(self):
        ip = self.lineEdit.text()
        self.inter.joinMeeting(ip)

class CreateWidget(QWidget):
    def __init__(self,inter):
        QWidget.__init__(self)
        ipLabel = QLabel("ip:"+inter.getIp())
        layout = QHBoxLayout()
        layout.addWidget(ipLabel)
        self.setLayout(layout)
        inter.createMeeting()
        

#这是初始界面
#界面里选择是创建会议，还是加入会议
class InitWidget(QWidget):
    def __init__(self, createButtonClicked, joinButtonClicked):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        createButton = QPushButton("创建会议")
        createButton.clicked.connect(createButtonClicked)
        layout.addWidget(createButton)
        joinButton = QPushButton("加入会议")
        layout.addWidget(joinButton)
        joinButton.clicked.connect(joinButtonClicked)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.inter = Interface()
        initWidget = InitWidget(self.toCreateWidget, self.toJoinWidget)
        self.setCentralWidget(initWidget)
    
    def toJoinWidget(self):
        self.setCentralWidget(JoinWidget(self.inter))
    def toCreateWidget(self):
        self.setCentralWidget(CreateWidget(self.inter))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()