from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.image = QImage("a.png")
        transform = QTransform()
        self.transform = transform
    
    def keyPressEvent(self, keyEvent):
        transform = QTransform()
        if keyEvent.key() == Qt.Key_Up:
            self.translate(0,8)
        if keyEvent.key() == Qt.Key_Down:
            self.translate(0,-8)
        if keyEvent.key() == Qt.Key_R:
            self.rotate(1)
        if keyEvent.key() == Qt.Key_T:
            self.rotate(-1)
        if keyEvent.key() == Qt.Key_S:
            self.scale(1.01)
        if keyEvent.key() == Qt.Key_D:
            self.scale(0.99)

    def translate(self,dx,dy):
        transform = QTransform()
        transform.translate(dx,dy)
        self.transform *= transform
        self.repaint()
    def rotate(self,angle):
        transform = QTransform()
        transform.rotate(angle)
        self.transform *= transform
        self.repaint()
    def scale(self,ratio):
        transform = QTransform()
        transform.scale(ratio,ratio)
        self.transform *= transform
        self.repaint()
    def paintEvent(self, paintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing,True)

        image = self.image
        transform = QTransform()
        transform.translate(self.width()/2,self.height()/2)
        transform = self.transform * transform
        painter.setTransform(transform)

        painter.drawImage(-image.width()/2,-image.height()/2,image)

app = QApplication(sys.argv)
win = Window()
win.show()
app.exec_()
