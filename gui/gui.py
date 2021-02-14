from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.image = QImage("a.png")
        self.translateX = 0
        self.translateY = 0
        self.rotateAngle = 0
        self.scaleRatio = 1
    
    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_S:
            self.translateY += 10
    def paintEvent(self, paintEvent):
        painter = QPainter(self)

        image = self.image
        painter.translate(self.width()/2,self.height()/2)
        painter.translate(self.translateX,self.translateY)
        painter.rotate(self.rotateAngle)
        painter.scale(self.scaleRatio,self.scaleRatio)

        painter.drawImage(-image.width()/2,-image.height()/2,image)

app = QApplication(sys.argv)
win = Window()
win.show()
app.exec_()
