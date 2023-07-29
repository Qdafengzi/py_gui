# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel, QApplication, QWidget

app = QApplication(sys.argv)
Form = QWidget()
Form.setWindowTitle("pyGui")
Form.resize(500, 500)
label = QtWidgets.QLabel(Form)
label.setText("Hello world")


Form.show()

app.exec()
