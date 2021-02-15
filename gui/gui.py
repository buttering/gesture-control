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
            transform.translate(0,8)
            self.repaint()
        if keyEvent.key() == Qt.Key_Down:
            transform.translate(0,-8)
            self.repaint()
        if keyEvent.key() == Qt.Key_R:
            transform.rotate(1)
            self.repaint()
        if keyEvent.key() == Qt.Key_T:
            transform.rotate(-1)
            self.repaint()
        if keyEvent.key() == Qt.Key_S:
            transform.scale(1.01,1.01)
            self.repaint()
        if keyEvent.key() == Qt.Key_D:
            transform.scale(0.99,0.99)
            self.repaint()
        self.transform *= transform
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
