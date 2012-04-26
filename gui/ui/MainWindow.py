# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Tue Apr 24 09:09:42 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1001, 578)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_4 = QtGui.QMenu(self.menubar)
        self.menu_4.setObjectName(_fromUtf8("menu_4"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.exit_menu = QtGui.QAction(MainWindow)
        self.exit_menu.setObjectName(_fromUtf8("exit_menu"))
        self.client_search_menu = QtGui.QAction(MainWindow)
        self.client_search_menu.setObjectName(_fromUtf8("client_search_menu"))
        self.client_add_menu = QtGui.QAction(MainWindow)
        self.client_add_menu.setObjectName(_fromUtf8("client_add_menu"))
        self.stuff_add_menu = QtGui.QAction(MainWindow)
        self.stuff_add_menu.setObjectName(_fromUtf8("stuff_add_menu"))
        self.order_search_menu = QtGui.QAction(MainWindow)
        self.order_search_menu.setObjectName(_fromUtf8("order_search_menu"))
        self.order_add_menu = QtGui.QAction(MainWindow)
        self.order_add_menu.setObjectName(_fromUtf8("order_add_menu"))
        self.menu.addAction(self.exit_menu)
        self.menu_2.addAction(self.client_add_menu)
        self.menu_2.addAction(self.client_search_menu)
        self.menu_4.addAction(self.order_add_menu)
        self.menu_4.addAction(self.order_search_menu)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exit_menu, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "Файл", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_2.setTitle(QtGui.QApplication.translate("MainWindow", "Клиенты", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_4.setTitle(QtGui.QApplication.translate("MainWindow", "Заказы", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_menu.setText(QtGui.QApplication.translate("MainWindow", "Выход", None, QtGui.QApplication.UnicodeUTF8))
        self.client_search_menu.setText(QtGui.QApplication.translate("MainWindow", "Поиск", None, QtGui.QApplication.UnicodeUTF8))
        self.client_add_menu.setText(QtGui.QApplication.translate("MainWindow", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.stuff_add_menu.setText(QtGui.QApplication.translate("MainWindow", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.order_search_menu.setText(QtGui.QApplication.translate("MainWindow", "Поиск", None, QtGui.QApplication.UnicodeUTF8))
        self.order_add_menu.setText(QtGui.QApplication.translate("MainWindow", "Новый заказ", None, QtGui.QApplication.UnicodeUTF8))

