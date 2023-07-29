# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QApplication


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setWindowTitle("android ")
        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.ui()
        # 接收有所有的键盘事件
        self.grabKeyboard()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Tab:
            print("按下了tab")

        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_S:
            print("command + s")

        #     多个修饰键 + 普通键
        if event.modifiers() == Qt.KeyboardModifier.ShiftModifier | Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_A:
            print("command + shift + A")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
