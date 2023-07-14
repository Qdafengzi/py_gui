# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("android ")
        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.grview = QtWidgets.QGraphicsView(self)
        self.grview.setGeometry(0, 0, 300, 300)
        scene = QtWidgets.QGraphicsScene()
        scene.setSceneRect(0,0,200,200)
        img = QtGui.QPixmap('./img/logo.png')

        img1 = img.scaled(200,50)
        qitem1 = QtWidgets.QGraphicsPixmapItem(img1)

        img2 = img.scaled(100,150)
        qitem2 = QtWidgets.QGraphicsPixmapItem(img2)
        scene.addItem(qitem1)
        scene.addItem(qitem2)
        self.grview.setScene(scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
