# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.grview = None
        self.setWindowTitle("android ")
        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.grview = QtWidgets.QGraphicsView(self)
        gw = 260
        gh = 200
        self.grview.setGeometry(20, 20, gw, gh)
        senece = QtWidgets.QGraphicsScene(self)

        img_w = 120  # 顯示圖片的寬度
        img_h = 160
        img = QtGui.QPixmap('../img/logo.png')
        img = img.scaled(img_w, img_h)

        x = 20  # 左上角 x 座標
        y = 20  # 左上角 y 座標
        dx = int((gw - img_w) / 2) - x  # 修正公式
        dy = int((gh - img_h) / 2) - y
        senece.setSceneRect(dx, dy, img_w, img_h)
        senece.addPixmap(img)
        self.grview.setScene(senece)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
