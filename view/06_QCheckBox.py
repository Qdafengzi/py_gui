# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("pyGui")
window.resize(500, 500)


checkBox = QCheckBox("&Python",window)
# 三态
checkBox.setTristate(True)
# checkBox.setCheckState(Qt.CheckState.Checked)
checkBox.setCheckState(Qt.CheckState.Unchecked)
# checkBox.setCheckState(Qt.CheckState.PartiallyChecked)
# checkBox.setText("哈哈哈")

checkBox.stateChanged.connect(lambda val :print(val))

window.show()

app.exec()
