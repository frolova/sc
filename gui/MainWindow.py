# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui
import gui

# Import the compiled UI module
from ui.MainWindow import Ui_MainWindow
from gui.AddClientWidget import AddClientWidget
from gui.OrdersWidget import OrdersWidget
from gui.AddOrderWidget import AddOrderWidget

class MainWindow(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.setOption(QMdiArea.DontMaximizeSubWindowOnActivation, True)
        self.user = user
        QObject.connect(self.ui.client_add_menu, SIGNAL("triggered()"), self, SLOT("show_add_client_widget()"))
        QObject.connect(self.ui.order_search_menu, SIGNAL("triggered()"), self, SLOT("show_orders_widget()"))
        QObject.connect(self.ui.order_add_menu, SIGNAL("triggered()"), self, SLOT("show_add_order_widget()"))


    @pyqtSlot()
    def show_add_client_widget(self):
        frame = QMdiSubWindow()
        widget = AddClientWidget(self)
        widget.setWindowModality(2)
        frame.setWidget(widget)
        frame.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.mdiArea.addSubWindow(widget)
        widget.show()

    @pyqtSlot()
    def show_add_order_widget(self):
        frame = QMdiSubWindow()
        widget = AddOrderWidget(self)
        widget.setWindowModality(2)
        frame.setWidget(widget)
        frame.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.mdiArea.addSubWindow(widget)
        widget.show()

    @pyqtSlot()
    def show_orders_widget(self):
        frame = QMdiSubWindow()
        widget = OrdersWidget(self)
        widget.setWindowModality(2)
        frame.setWidget(widget)
        frame.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.mdiArea.addSubWindow(widget)
        widget.show()

