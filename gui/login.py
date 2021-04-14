#login.py

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: jyroy
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from Header import TitleBar,FramelessWindow


StyleSheet = """
/*最小化最大化关闭按钮通用默认背景*/
#buttonMinimum,#buttonMaximum,#buttonClose {
    border: none;
}
/*悬停*/
#buttonMinimum:hover,#buttonMaximum:hover {

    color: white;
}
#buttonClose:hover {
    color: white;
}
/*鼠标按下不放*/
#buttonMinimum:pressed,#buttonMaximum:pressed {

}
#buttonClose:pressed {
    color: white;

}
"""   #标题栏Button的样式

StyleSheet_2 = """
QComboBox{
        height: 20px;
        border-radius: 4px;
        border: 1px solid rgb(111, 156, 207);
        margin: 10px;
        background: white;
}
QComboBox:enabled{
        color: grey;
}
QComboBox:!enabled {
        color: rgb(80, 80, 80);
}
QComboBox:enabled:hover, QComboBox:enabled:focus {
        color: rgb(51, 51, 51);
}
QComboBox::drop-down {
        background: transparent;
}
QComboBox::drop-down:hover {
        background: lightgrey;
}

QComboBox QAbstractItemView {
        border: 1px solid rgb(111, 156, 207);
        background: white;
        outline: none;
}

 QLineEdit {
        border-radius: 4px;
        height: 20px;
        border: 1px solid rgb(111, 156, 207);
        margin: 10px;
        background: white;
}
QLineEdit:enabled {
        color: rgb(84, 84, 84);
}
QLineEdit:enabled:hover, QLineEdit:enabled:focus {
        color: rgb(51, 51, 51);
}
QLineEdit:!enabled {
        color: rgb(80, 80, 80);
}


"""   #QComobox和QLineEdite的样式

StyleSheet_btn = """
QPushButton{
    height:30px;
    background-color: transparent;
    color: grey;
    border: 2px solid #555555;
    border-radius: 6px;

}
QPushButton:hover {
    background-color: white;
    border-radius: 6px;

}
"""  #登录Button的样式

class loginWnd(QWidget):
    '''登录窗口'''
    def __init__(self, *args, **kwargs):
        super(loginWnd, self).__init__()
        self._layout = QVBoxLayout(spacing=0)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setAutoFillBackground(True)
        self.setWindowOpacity(0.1)

        self.setLayout(self._layout)

        self._setup_ui()

    def _setup_ui(self):

        self.main_layout = QGridLayout()

        self.main_layout.setAlignment(Qt.AlignCenter)

        name_label = QLabel('用户名')
        name_label.setStyleSheet("color:grey;")
        passwd_label = QLabel('密码')
        passwd_label.setStyleSheet("color:grey;")

        name_box = QComboBox()
        name_box.setEditable(True)
        passwd_box = QLineEdit()
        passwd_box.setEchoMode(QLineEdit.Password)
        name_box.setStyleSheet(StyleSheet_2)
        passwd_box.setStyleSheet(StyleSheet_2)

        label = QLabel()

        login_btn = QPushButton("登录")
        login_btn.setStyleSheet(StyleSheet_btn)

        self.main_layout.addWidget(name_label,0,0,1,1)
        self.main_layout.addWidget(passwd_label,1,0,1,1)
        self.main_layout.addWidget(name_box,0,1,1,2)
        self.main_layout.addWidget(passwd_box,1,1,1, 2)
        self.main_layout.addWidget(label,3,0,1,3)
        self.main_layout.addWidget(login_btn,4,0,1,3)

        self._layout.addLayout(self.main_layout)

def main():
    ''':return:'''

    app = QApplication(sys.argv)

    mainWnd = FramelessWindow()
    mainWnd.setWindowTitle('欢迎窗口login')
    mainWnd.setWindowIcon(QIcon('Qt.ico'))
    mainWnd.setFixedSize(QSize(500,400))  #因为这里固定了大小，所以窗口的大小没有办法任意调整，想要使resizeWidget函数生效的话要把这里去掉，自己调节布局和窗口大小
    mainWnd.setWidget(loginWnd(mainWnd))  # 把自己的窗口添加进来
    mainWnd.show()

    app.exec()

if __name__ == '__main__':
    main()