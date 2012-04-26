# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddClientWidget.ui'
#
# Created: Thu Apr 26 20:47:51 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddClientWidget(object):
    def setupUi(self, AddClientWidget):
        AddClientWidget.setObjectName(_fromUtf8("AddClientWidget"))
        AddClientWidget.resize(309, 255)
        AddClientWidget.setWindowTitle(QtGui.QApplication.translate("AddClientWidget", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        AddClientWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        AddClientWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_2 = QtGui.QGridLayout(AddClientWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widget = QtGui.QWidget(AddClientWidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.birthdate = QtGui.QDateEdit(self.widget)
        self.birthdate.setObjectName(_fromUtf8("birthdate"))
        self.gridLayout.addWidget(self.birthdate, 4, 1, 1, 1)
        self.surname = QtGui.QLineEdit(self.widget)
        self.surname.setObjectName(_fromUtf8("surname"))
        self.gridLayout.addWidget(self.surname, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setText(QtGui.QApplication.translate("AddClientWidget", "Отчество", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.phone_num = QtGui.QLineEdit(self.widget)
        self.phone_num.setObjectName(_fromUtf8("phone_num"))
        self.gridLayout.addWidget(self.phone_num, 5, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setText(QtGui.QApplication.translate("AddClientWidget", "Дата рождения", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lastname = QtGui.QLineEdit(self.widget)
        self.lastname.setObjectName(_fromUtf8("lastname"))
        self.gridLayout.addWidget(self.lastname, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setText(QtGui.QApplication.translate("AddClientWidget", "Телефон", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setText(QtGui.QApplication.translate("AddClientWidget", "Пол", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.name = QtGui.QLineEdit(self.widget)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setText(QtGui.QApplication.translate("AddClientWidget", "Имя", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setText(QtGui.QApplication.translate("AddClientWidget", "Фамилия", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.Male = QtGui.QRadioButton(self.frame)
        self.Male.setGeometry(QtCore.QRect(10, 10, 31, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Male.sizePolicy().hasHeightForWidth())
        self.Male.setSizePolicy(sizePolicy)
        self.Male.setText(QtGui.QApplication.translate("AddClientWidget", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.Male.setChecked(True)
        self.Male.setObjectName(_fromUtf8("Male"))
        self.radioButton_2 = QtGui.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 10, 31, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setText(QtGui.QApplication.translate("AddClientWidget", "Ж", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout.addWidget(self.frame, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(AddClientWidget)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddClientWidget.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(AddClientWidget)
        AddClientWidget.setTabOrder(self.surname, self.name)
        AddClientWidget.setTabOrder(self.name, self.lastname)
        AddClientWidget.setTabOrder(self.lastname, self.Male)
        AddClientWidget.setTabOrder(self.Male, self.radioButton_2)
        AddClientWidget.setTabOrder(self.radioButton_2, self.birthdate)
        AddClientWidget.setTabOrder(self.birthdate, self.phone_num)
        AddClientWidget.setTabOrder(self.phone_num, self.buttonBox)

    def retranslateUi(self, AddClientWidget):
        pass

