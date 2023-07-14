# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label2 = None
        self.label = None
        self.setWindowTitle("android ")
        self.resize(600, 600)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")
        self.label.setGeometry(100, 0, 100, 40)
        self.label.setWordWrap(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.label.setStyleSheet('''
                    background:#ccc;
                    color:#fcc;
                    font-size:20px;
                    font-weight:bold;
                    border:2px dashed #000;
                    padding:2px;
                    text-align:center;
                ''')

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Hello World hello ")
        self.label2.setGeometry(100, 50, 200, 200)
        self.label2.setStyleSheet('background:#ffc')
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label2.setContentsMargins(0, 0, 0, 0)  # 設定邊界
        self.label2.setWordWrap(True)  # 可以換行

        font = QtGui.QFont()
        font.setFamily('Verdana')  # 設定字體
        font.setPointSize(10)  # 文字大小
        font.setBold(True)  # 粗體
        font.setItalic(True)  # 斜體
        font.setStrikeOut(True)  # 刪除線
        font.setUnderline(True)  # 底線
        self.label2.setFont(font)  # 設定文字樣式

        img = QtGui.QImage('mona.jpg')  # 讀取圖片
        self.label2.setPixmap(QtGui.QPixmap.fromImage(img))  # 加入圖片


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
