# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import *


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button = None
        self.label = None
        self.setWindowTitle("android ")
        self.resize(800, 800)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")

        self.button = QPushButton(self)
        self.button.setText("1")
        self.button.move(100, 0)

        def plus():
            num = int(self.button.text()) + 1
            self.button.setText(str(num))
            print("按钮被点击了", num)
            # print("按钮被点击了")

        self.button.pressed.connect(plus)

        # self.button.setText("a&bc")
        self.button.setShortcut("Ctrl+A")
        self.button.setAutoRepeat(True)
        # self.button.setAutoRepeatInterval(100)
        self.button.setAutoRepeatDelay(1000)
        self.button.setAutoRepeatInterval(100)
        self.button.setStyleSheet("QPushButton:pressed{background-color:red}")

        # self.button.setDown(True)
        # self.button.setChecked(True)

        self.checkBox = QCheckBox(self)
        self.checkBox.setText("这是一个checkBox")
        self.checkBox.move(100, 50)

        print(self.checkBox.isCheckable())

        self.riButton = QRadioButton(self)
        self.riButton.setText("这是一个RadioButton")
        self.riButton.move(100, 100)


        for i in range(3):
            button = QPushButton(self)
            button.setText("buton")
            button.move(200,200+ 60*i)
            button.setCheckable(True)
            button.setAutoExclusive(False)

            # 模拟用户点击
            # button.animateClick()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
