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
        self.r_male = QRadioButton("男", self)
        self.r_male.move(100, 50)
        self.r_female = QRadioButton("女", self)
        self.r_female.move(100, 100)
        self.group_sex = QButtonGroup(self)
        self.group_sex.addButton(self.r_male, 1)
        self.group_sex.addButton(self.r_female, 2)
        self.r_female.setChecked(True)

        print(self.group_sex.buttons())
        print(self.group_sex.checkedButton())

        self.r_yes = QRadioButton("yes", self)
        self.r_yes.move(200, 50)
        self.r_no = QRadioButton("no", self)
        self.r_no.move(200, 100)

        self.group_res = QButtonGroup(self)
        self.group_res.addButton(self.r_yes)
        self.group_res.addButton(self.r_no)
        self.group_res.setId(self.r_yes,3)
        self.group_res.setId(self.r_no,4)

        #选择状态变化的时候
        self.group_res.buttonToggled.connect(lambda val:print(val))
        # 点击
        self.group_res.buttonClicked.connect(lambda val:print(val))

        print(self.group_res.id(self.r_yes))
        print(self.group_res.id(self.r_no))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
