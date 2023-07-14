# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6.QtWidgets import QLabel, QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
label = QLabel(window)
label.setText("Hello World")
window.setWindowTitle("pyGui")
window.resize(500, 500)
window.show()

app.exec()
