# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import model
#from utils import _date_from_str
from sqlalchemy.exc import SQLAlchemyError
from datetime import date
from model import Session, Client, Order

import ui
from ui.AddOrderWidget import Ui_AddOrderWidget


class AddOrderWidget(QFrame):
    def __init__(self, parent):
        self.parent = parent
        QFrame.__init__(self)
        self.ui = Ui_AddOrderWidget()
        self.ui.setupUi(self)
        self.draw_client_combo()
        QObject.connect(self.ui.add_client_btn, SIGNAL("clicked()"), self.parent, SLOT('show_add_client_widget()'))
        QObject.connect(self.ui.buttonBox, SIGNAL("accepted()"), self.add_order)


    def add_order(self):
        s = Session()
        ord = Order()
        ord.manager_id = self.parent.user.id
        ord.device =  unicode(self.ui.device.text())
        ord.description =  unicode(self.ui.description)
        ord.client_id = s.query(Client).filter_by(id=unicode(self.ui.client.itemText(self.ui.client.currentIndex())).split()[0]).one().id
        s.add(ord)
        s.commit()
        s.close()
        self.close()

    def draw_client_combo(self):
        combo = self.ui.client
        s = Session()
        clients = s.query(Client).all()
        s.close()
        combo.clear()
        for cl in clients:
            combo.addItem('%i %s %s'%(cl.id, cl.surname, cl.name))
        #QObject.connect(self.ui.manufacter_combo, SIGNAL("currentIndexChanged(int)"), self.setManufacter)
        #self.setManufacter(0)