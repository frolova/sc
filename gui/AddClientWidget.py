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
from ui.AddClientWidget import Ui_AddClientWidget


class AddClientWidget(QFrame):
    def __init__(self, parent):
        self.parent = parent
        QFrame.__init__(self)
        self.ui = Ui_AddClientWidget()
        self.ui.setupUi(self)
        QObject.connect(self.ui.buttonBox, SIGNAL("accepted()"), self.add_client)

    def add_client(self):
        new_client = model.Client()
        new_client.name = unicode(self.ui.name.text())
        new_client.surname = unicode(self.ui.surname.text())
        new_client.lastname = unicode(self.ui.lastname.text())
        new_client.birthday = date(self.ui.birthdate.date().year(), self.ui.birthdate.date().month(), self.ui.birthdate.date().day())
        new_client.male = self.ui.Male.isChecked()
        new_client.phone = unicode(self.ui.phone_num.text())
        s = model.Session()
        s.add(new_client)
        try:
            s.commit()
            self.close()
        except SQLAlchemyError as e:
            print e
            QMessageBox.critical(self, QString.fromUtf8('Ошибка'),
                QString.fromUtf8("Неверный ввод! Попробуйте снова!"), QMessageBox.Ok |
                                         QMessageBox.Ok)
        finally:
            s.close()