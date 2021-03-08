
from PyQt5.QtWidgets import *
import sys

# 在引入父目录的模块之前加上如下代码：
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
#os.pardir:Linux下相当于"../"
#————————————————
#版权声明：本文为CSDN博主「孤独的侠客」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/chenyunqiang/article/details/104648942

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
        self.inter.joinMeeting(self.lineEdit.text())

class CreateWidget(QWidget):
    def __init__(self,inter):
        QWidget.__init__(self)
        meetingId = inter.createMeeting()
        ipLabel = QLabel("ip:"+meetingId)
        layout = QHBoxLayout()
        layout.addWidget(ipLabel)
        self.setLayout(layout)
        
        

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