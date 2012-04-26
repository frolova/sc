# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from model import Staff, Session

import ui
import gui

# Import the compiled UI module
from ui.LoginWindow import Ui_LoginWindow
from gui.MainWindow import MainWindow

class LoginWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui=Ui_LoginWindow()
        self.ui.setupUi(self)
        QObject.connect(self.ui.buttonBox, SIGNAL("accepted()"), self, SLOT("login()"))
#        QObject.connect(self.ui.order_search_menu, SIGNAL("triggered()"), self, SLOT("show_orders_widget()"))


    @pyqtSlot()
    def login(self):
        s = Session()
        res = s.query(Staff).filter_by(login=unicode(self.ui.login.text()),
            passwd=unicode(self.ui.password.text())).all()
        if len(res):
            self.mv = MainWindow(res[0])
            self.mv.show()
            self.close()
        s.close()
