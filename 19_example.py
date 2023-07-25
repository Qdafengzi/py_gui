# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.button_min = None
        self.button_max = None
        self.button_close = None
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("顶层窗口案例")
        # win.setWindowOpacity(0.8)
        self.resize(400, 400)

        self.top_margin = 10
        self.button_w = 80
        self.button_h = 40

        self.setupUi()

    def setupUi(self):
        self.button_close = QPushButton(self)
        self.button_close.setText("Close")

        self.button_max = QPushButton(self)
        self.button_max.setText("Max")

        self.button_min = QPushButton(self)
        self.button_min.setText("Min")

        def close():
            self.close()

        self.button_close.pressed.connect(close)

        def maxSize():
            if self.isMaximized():
                self.showNormal()
                self.button_max.setText("最大化")
            else:
                self.showMaximized()
                self.button_max.setText("恢复")

        self.button_max.pressed.connect(maxSize)

        def minSize():
            self.showMinimized()

        self.button_min.pressed.connect(minSize)

    def resizeEvent(self, a0):
        self.button_close.resize(self.button_w, self.button_h)
        button_close_width = self.button_close.width()
        self.button_close.move(self.width() - button_close_width, self.top_margin)

        self.button_max.resize(self.button_w, self.button_h)
        self.button_max.move(self.button_close.x() - self.button_max.width(), self.top_margin)

        self.button_min.resize(self.button_w, self.button_h)
        self.button_min.move(self.button_max.x() - self.button_min.width(), self.top_margin)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    app.exec()
