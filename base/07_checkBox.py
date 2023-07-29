# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.arr = None
        self.label = None
        self.setWindowTitle("android ")
        self.resize(600, 600)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.arr = [''] * 3
        self.label = QtWidgets.QLabel(self)
        self.label.setText("label")
        self.label.setGeometry(300, 300, 100, 100)

        style = '''
                    QCheckBox {
                        color: #00f;
                    }
                    QCheckBox:hover {
                        color: #f00;
                    }
                    QCheckBox:checked {
                        color: #fff;
                        background: #000;
                    }
                '''


        self.checkBox_a = QtWidgets.QCheckBox(self)
        self.checkBox_a.setText("JAVA")
        self.checkBox_a.setGeometry(10, 10, 100, 30)
        self.checkBox_a.setChecked(True)
        self.checkBox_a.setStyleSheet(style)
        self.checkBox_a.clicked.connect(lambda: self.showText(self.checkBox_a, 0))


        self.checkBox_b = QtWidgets.QCheckBox(self)
        self.checkBox_b.setText("Kotlin")
        self.checkBox_b.setGeometry(10, 40, 100, 30)
        self.checkBox_b.setStyleSheet(style)
        self.checkBox_b.clicked.connect(lambda: self.showText(self.checkBox_b, 1))

        self.checkBox_c = QtWidgets.QCheckBox(self)
        self.checkBox_c.setText("C#")
        # self.checkBox_c.setDisabled(True)
        self.checkBox_c.setGeometry(10, 70, 100, 30)
        self.checkBox_c.setStyleSheet(style)
        self.checkBox_c.clicked.connect(lambda: self.showText(self.checkBox_c, 2))

    def showText(self, cb, i):
        if cb.isChecked():
            self.arr[i] = cb.text()  # 如果該按鈕是勾選狀態，在串列的指定位置放入文字
        else:
            self.arr[i] = ''  # 如果該按鈕是勾選狀態，在串列的指定位置放入空字串
        output = ''.join(self.arr)  # 組合串列內容為文字
        self.label.setText(output)  # label 顯示文字



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
