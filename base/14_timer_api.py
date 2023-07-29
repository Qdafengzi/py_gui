# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication, QLabel


class MyObject(QObject):
    def timerEvent(self, a0):
        print(a0, "1")


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(MyLabel, self).__init__(*args, **kwargs)
        self.setText("10")
        self.timer_id = self.startTimer(1000)

    def timerEvent(self, a0):
        text = int(self.text())
        text -= 1
        if (text == 0):
            self.killTimer(self.timer_id)
        self.setText(str(text))


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setWindowTitle("android ")
        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = MyLabel(self)
        # obj = MyObject(self)
        # timer_id = obj.startTimer(1000)

        # obj.killTimer(timer_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
