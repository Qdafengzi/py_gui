# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import *


class Window(QWidget):
    def contextMenuEvent(self, env):
        print("默认上下文菜单")
        menu = QMenu(self)
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

        # self.mapToGlobal(env.globalPos())
        menu.exec(env.globalPos())


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

        self.button = QPushButton(self)
        self.button.setText("菜单")
        self.button.move(50, 50)

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

        self.button.setMenu(menu)

        self.commandBbutton = QCommandLinkButton(self)
        self.commandBbutton.setText("标题")
        self.commandBbutton.move(200, 200)
        self.commandBbutton.setDescription("描述")
        self.commandBbutton.setIcon(QIcon("../img/logo.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()


    def aa():
        print("右键自定义菜单")


    # 自定义菜单
    Form.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
    Form.customContextMenuRequested.connect(aa)

    Form.show()
    sys.exit(app.exec())
