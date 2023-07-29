# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction
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
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")

        self.toolbutton = QToolButton(self)
        self.toolbutton.move(50, 50)
        self.toolbutton.setText("文本")
        self.toolbutton.setToolTip("这是一个菜单按钮")
        self.toolbutton.setIcon(QIcon("../img/logo.png"))

        # Qt.ToolButtonStyle.ToolButtonIconOnly	Icon only, no text
        # Qt.ToolButtonStyle.ToolButtonTextOnly	Text only, no icon
        # Qt.ToolButtonStyle.ToolButtonTextBesideIcon	Icon and text, with text beside the icon
        # Qt.ToolButtonStyle.ToolButtonTextUnderIcon	Icon and text, with text under the icon
        # Qt.ToolButtonStyle.ToolButtonFollowStyle	Follow the host desktop style
        # self.toolbutton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        # self.toolbutton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolbutton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        # self.toolbutton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        # self.toolbutton.setArrowType(Qt.ArrowType.DownArrow)
        self.toolbutton.setArrowType(Qt.ArrowType.UpArrow)

        self.toolbutton.setAutoRaise(True)

        menu = QMenu()
        action_new = QAction(QIcon("../img/logo.png"), "新建", menu)
        # action.setText("新建")
        # action.setIcon(QIcon("../img/logo.png"))
        action_new.triggered.connect(lambda: print("新建"))
        menu.addAction(action_new)

        action_open = QAction(QIcon("../img/logo.png"), "打开", menu)
        action_open.triggered.connect(lambda: print("打开"))
        menu.addAction(action_open)

        childMenu = QMenu(menu)
        childMenu.setTitle("最近打开")
        action_child = QAction("子菜单的item", childMenu)
        action_child2 = QAction("子菜单的item2", childMenu)

        childMenu.addAction(action_child)
        childMenu.addAction(action_child2)
        menu.addMenu(childMenu)

        menu.addSeparator()

        action_exist = QAction(QIcon("../img/logo.png"), "退出", menu)
        action_exist.triggered.connect(lambda: print("退出"))
        menu.addAction(action_exist)

        # self.toolbutton.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolbutton.setMenu(menu)
        def fun():
            print("test")

        self.toolbutton.triggered.connect(fun)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
