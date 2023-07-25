# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setWindowTitle("android ")
        self.resize(500, 500)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QLabel(self)
        self.label.setText("Hello World")
        self.label.hide()
        self.label.move(100, 50)

        self.edit = QLineEdit(self)
        self.edit.move(100, 100)

        self.button = QPushButton(self)
        self.button.move(100, 150)
        self.button.setText("登录")
        self.button.setEnabled(False)

        def textChange(text):
            self.button.setEnabled(len(text) > 0)

        self.edit.textChanged.connect(textChange)

        def login():
            if self.edit.text() == "qt":
                self.label.show()
                self.label.setText("登录成功")
            else:
                self.label.show()
                self.label.setText("登录失败")
        self.button.clicked.connect(login)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
