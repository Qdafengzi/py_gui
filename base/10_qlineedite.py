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
        self.label.setText("显示密码")

        self.input = QtWidgets.QLineEdit(self)
        self.input.move(20,20)
        self.input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.input.setText("123456")
        self.input.setMaxLength(6)
        self.input.setStyleSheet('''
        QLineEdit {
            border:1px solid #000;
        }
        QLineEdit {
            border:2px solid #f00;
            background:#ff0;
        }
        
        ''')
        self.input.textChanged.connect(self.textChange)

        self.input2 = QtWidgets.QLineEdit(self)
        self.input2.setGeometry(20,50,100,20)

    def textChange(self):
        self.label.setText(self.input.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
