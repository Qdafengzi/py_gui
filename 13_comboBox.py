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
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItems(["A", "B", "C", "D", "E"])
        self.comboBox.setGeometry(20, 20, 80, 20)

        self.comboBox.setCurrentIndex(1)  # 預先顯示第二個選項 ( 第一個為 0 )
        # self.comboBox.setCurrentText('D')  # 如果選項文字為 D，則顯示 D

        self.comboBox.addItem('apple')  # 在最後方添加 apple 選項
        self.comboBox.removeItem(2)  # 移除第三個選項 C
        self.comboBox.insertItem(0, 'ok')  # 在最前方加入 ok 為第一個選項


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
