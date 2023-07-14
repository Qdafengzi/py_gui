# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.btn2 = None
        self.label = None
        self.button3 = None
        self.button2 = None
        self.button = None
        self.setWindowTitle("android ")
        self.resize(600, 600)
        self.setUpdatesEnabled(True)
        self.a = 0
        self.ui()

    def ui(self):
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("点我")
        self.button.move(50, 30)
        self.button.setStyleSheet('''
         QPushButton {
        font-size:20px;
        color: #f00;
        background: #ff0;
        border: 2px solid #000;
    }
    QPushButton:hover {
        color: #ff0;
        background: #f00;
    }
        ''')

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setText("增加数字")
        self.button2.setGeometry(50, 60, 100, 50)
        self.button2.setStyleSheet('''
              background:#fc0;
              color:#f00;
              font-size:20px;
              border:2px solid #000;
        ''')
        self.button2.clicked.connect(self.showNum)  # 點擊時執行 show 函式

        self.button3 = QtWidgets.QPushButton(self)
        self.button3.setText("按钮3")
        self.button3.setGeometry(50, 120, 100, 50)
        self.button3.setDisabled(True)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('复位')
        self.btn2.setGeometry(200, 60, 50, 30)
        self.btn2.clicked.connect(self.reset)  # 使用 lambda 函式

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(10, 10, 100, 20)
        self.label.setText("0")
        self.label.move(50, 10)

    def showText(self, text):
        self.label.setText(text)

    def showNum(self):
        self.a = self.a + 1
        self.label.setText(str(self.a))

    def reset(self):
        self.a = 0
        self.label.setText(str(self.a))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
