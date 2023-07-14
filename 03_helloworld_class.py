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
        self.setWindowTitle("android")

        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")
        self.label.setStyleSheet('color:#eee;font-size:30px;background:#ffc')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.setStyleSheet('background:#fcc;')
    Form.show()
    app.exec()
