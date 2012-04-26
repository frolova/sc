# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrdersWidget.ui'
#
# Created: Tue Apr 24 14:19:39 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OrdersWidget(object):
    def setupUi(self, OrdersWidget):
        OrdersWidget.setObjectName(_fromUtf8("OrdersWidget"))
        OrdersWidget.resize(654, 391)
        OrdersWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        OrdersWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(OrdersWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.orders_table = QtGui.QTableWidget(OrdersWidget)
        self.orders_table.setRowCount(1)
        self.orders_table.setColumnCount(1)
        self.orders_table.setObjectName(_fromUtf8("orders_table"))
        self.verticalLayout.addWidget(self.orders_table)
        self.frame = QtGui.QFrame(OrdersWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.new_order_btn = QtGui.QPushButton(self.frame)
        self.new_order_btn.setObjectName(_fromUtf8("new_order_btn"))
        self.gridLayout.addWidget(self.new_order_btn, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(530, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(OrdersWidget)
        QtCore.QMetaObject.connectSlotsByName(OrdersWidget)

    def retranslateUi(self, OrdersWidget):
        OrdersWidget.setWindowTitle(QtGui.QApplication.translate("OrdersWidget", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.new_order_btn.setText(QtGui.QApplication.translate("OrdersWidget", "Новый заказ", None, QtGui.QApplication.UnicodeUTF8))

