from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys

class PictureWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.image = QImage("a.png")
        transform = QTransform()
        self.transform = transform
        print("hhh")

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


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Picture")
        self.setMinimumSize(500,400)

        menuBar = QMenuBar()
        fileMenu = QMenu("文件",menuBar)
        openAction = QAction("打开",fileMenu)
        openAction.setStatusTip("打开一个图片")
        fileMenu.addAction(openAction)
        fileMenu.triggered[QAction].connect(self.fileTrigger)
        menuBar.addMenu(fileMenu) 
        self.setMenuBar(menuBar)

        self.pictureWidget = PictureWidget()
        self.setCentralWidget(self.pictureWidget)

    def fileTrigger(self,q):
        if q.text() == "打开":
            imageFilePath,filt = QFileDialog.getOpenFileName(self,"选择图片",".","images(*.png *jpeg *bmp)")
            self.pictureWidget.image = QImage(imageFilePath)

app = QApplication(sys.argv)
win = Window()
win.show()
app.exec_()
