# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowFlag(QtCore.Qt.WindowType.WindowContextHelpButtonHint)
    win.resize(500,500)
    win.setWindowTitle("状态栏的提示例子")
    win.statusBar()
    win.setStatusTip("我是状态栏的提示内容")

    label = QLabel(win)
    label.setText("这是一个标签")
    label.setToolTip("这是一个标签的控件")
    label.setStatusTip("停留在了标签上")
    # 2秒展示
    label.setToolTipDuration(2000)

    label.setWhatsThis("这是啥？这是一个标签啊")
    # label.statusTip()


    win.show()
    sys.exit(app.exec())
