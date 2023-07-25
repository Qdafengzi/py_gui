# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setWindowTitle("android ")
        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")

    def closeEvent(self, a0):
        print("窗口关闭")

    def showEvent(self, a0):
        print("窗口打开")

    def moveEvent(self, a0):
        print("窗口移动")

    def resizeEvent(self, a0):
        print("窗口大小改变了")

    def leaveEvent(self, a0):
        print("鼠标离开")

    def enterEvent(self, event):
        print("鼠标进入")

    def mousePressEvent(self, a0):
        print("鼠标按下")

    def mouseMoveEvent(self, a0):
        print("鼠标移动")

    def mouseDoubleClickEvent(self, a0):
        print("鼠标双击")

    def mouseReleaseEvent(self, a0):
        print("鼠标释放")

    def keyPressEvent(self, a0):
        print("keyPressEvent")

    def keyReleaseEvent(self, a0):
        print("按键被释放")

    def focusInEvent(self, a0):
        print("focusInEvent")    

    def focusOutEvent(self, a0):
        print("focusOutEvent")

    def dragMoveEvent(self, a0):
        print("dragMoveEvent")

    def dragEnterEvent(self, a0):
        print("dragEnterEvent")

    def dragLeaveEvent(self, a0):
        print("dragLeaveEvent")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
