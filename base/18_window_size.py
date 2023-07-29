# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.move_flag = False
        self.mouse_y = None
        self.mouse_x = None
        self.origin_y = None

        self.origin_x = None
        self.label = None
        self.setWindowTitle("android ")
        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")

    def mousePressEvent(self, a0):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()

    # icon = QIcon("../img/logo.png")
    # Form.setWindowIcon(icon)
    # Form.setWindowTitle("aaaa")
    # Form.setWindowOpacity(0.4)

    print(Form.windowState() == Qt.WindowState.WindowNoState)

    # Form.setWindowState(Qt.WindowState.WindowMinimized)
    # Form.setWindowState(Qt.WindowState.WindowMaximized)
    # Form.setWindowState(Qt.WindowState.WindowFullScreen)
    Form.setWindowState(Qt.WindowState.WindowActive)

    Form.show()
    app.exec()
