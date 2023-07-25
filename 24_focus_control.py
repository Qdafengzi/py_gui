# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QLineEdit


class Window(QWidget):
    def mousePressEvent(self, a0):
        self.focusNextChild()
        # self.focusPreviousChild()


app = QApplication(sys.argv)
window = Window()

window.setWindowTitle("pyGui")
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(100, 50)

le2 = QLineEdit(window)
le2.move(100, 100)

le3 = QLineEdit(window)
le3.move(100, 150)

# le3.setFocus()

# le3.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

# le3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
# le3.setFocusPolicy(Qt.FocusPolicy.TabFocus)

# 设置 获取焦点的顺序 1 3 2
QWidget.setTabOrder(le1, le3)
QWidget.setTabOrder(le3, le2)

window.show()

app.exec()
