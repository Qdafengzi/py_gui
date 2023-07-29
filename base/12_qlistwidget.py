# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets, QtGui
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
        self.listwidget = QtWidgets.QListWidget(self)
        self.listwidget.addItems(["A", "B", "C", "D", "E", "F", "G"])
        self.listwidget.setGeometry(20, 20, 200, 300)

        item = self.listwidget.takeItem(1)
        self.listwidget.removeItemWidget(item)

        self.listwidget.addItem("X")
        self.listwidget.insertItem(0, self.getItem("", "../img/logo.png"))

        item1 = self.listwidget.item(3)
        item1.setText("Ok")
        item1.setIcon(QtGui.QIcon("../img/logo.png"))

        # self.listwidget.setFlow(QtWidgets.QListView.Flow.LeftToRight)  # 改成水平顯示

    def getItem(self, text, icon):
        item = QtWidgets.QListWidgetItem()
        item.setText(text)
        item.setIcon(QtGui.QIcon(icon))
        return item


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    app.exec()
