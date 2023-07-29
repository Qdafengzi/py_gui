# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import *


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

        self.radiobutton = QRadioButton(self)
        self.radiobutton.move(50, 100)
        self.radiobutton.setText("男")
        # self.radiobutton.setShortcut("Alt+M")
        # self.radiobutton.setShortcut(QKeySequence("Alt+M"))
        # self.radiobutton.setShortcut(QKeySequence("Ctrl+P"))
        self.radiobutton.setShortcut('Ctrl+a')
        self.radiobutton.setChecked(True)
        self.radiobutton.toggled.connect(lambda isChecked:print(isChecked))

        self.radiobutton2 = QRadioButton("女-&Female", self)
        self.radiobutton.setShortcut("Alt+F")
        self.radiobutton2.move(50, 120)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
