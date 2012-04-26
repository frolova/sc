# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import model
#from utils import _date_from_str
from sqlalchemy.exc import SQLAlchemyError
from datetime import date

import ui
from ui.OrdersWidget import Ui_OrdersWidget
from model import Session, Order


class OrdersWidget(QFrame):
    def __init__(self, parent):
        self.parent = parent
        QFrame.__init__(self)
        self.ui = Ui_OrdersWidget()
        self.ui.setupUi(self)
        self.draw_table()

    def draw_table(self):
        s = Session()
        self.orders = s.query(Order).all()
        s.close()
        self.ui.orders_table.clear()
        self.ui.orders_table.setRowCount(1)
        self.ui.orders_table.setColumnCount(5)
        self.ui.orders_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Поломка'),
                                                        QString.fromUtf8('Дата приемки'), QString.fromUtf8('Клиент'),
                                                        QString.fromUtf8('Статус')])
        #self.ui.orders_table.resizeColumnsToContents()

        for order in self.orders:
            data = []
            data.append(str(order.id))
            data.append(QString.fromUtf8(order.device))
            data.append(str(order.get_ordered_date()))
            data.append(QString.fromUtf8(order.get_client().get_fio()))
            data.append(QString.fromUtf8(order.get_status(1).to_string()))
            for i in range(0,5):
                tableitem = QTableWidgetItem()
                tableitem.setText(data[i])
                tableitem.font = QFont("Arial", 10)
                tableitem.font.setBold(True)
                tableitem.textcolor = QColor("black")
                self.ui.orders_table.setItem(self.ui.orders_table.rowCount() - 1,i,tableitem)
            self.ui.orders_table.setRowCount(self.ui.orders_table.rowCount()+1)
        self.ui.orders_table.resizeColumnsToContents()