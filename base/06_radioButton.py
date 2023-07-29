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
        self.resize(600, 600)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("label")
        self.label.setGeometry(300, 300, 100, 100)

        self.radio_a = QtWidgets.QRadioButton(self)
        self.radio_a.setGeometry(30, 30, 100, 20)
        self.radio_a.setText('A')
        self.radio_a.setStyleSheet('''
        QRadioButton{
            color:#00f 
        }
         QRadioButton:hover{
            color:#f0f 
        }
        
        ''')

        self.radio_b = QtWidgets.QRadioButton(self)
        self.radio_b.setGeometry(30, 50, 100, 60)
        self.radio_b.setText('B')

        self.radio_group = QtWidgets.QButtonGroup(self)
        self.radio_group.addButton(self.radio_a, 1)
        self.radio_group.addButton(self.radio_b, 2)
        self.radio_group.buttonClicked.connect(self.showLabel)

        self.radio_c = QtWidgets.QRadioButton(self)
        self.radio_c.setGeometry(30, 80, 100, 60)
        self.radio_c.setText("C")
        # self.radio_c.setDisabled(False)

        self.radio_c.toggled.connect(lambda: self.toggledMethod(self.radio_c))  # 綁定函式

    def toggledMethod(self, rb):
        self.label.setText(rb.text() + ':' + str(rb.isChecked()))

    def showLabel(self):
        self.label.setText(str(self.radio_group.checkedId()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
