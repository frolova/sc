# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddOrderWidget.ui'
#
# Created: Thu Apr 26 14:32:44 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddOrderWidget(object):
    def setupUi(self, AddOrderWidget):
        AddOrderWidget.setObjectName(_fromUtf8("AddOrderWidget"))
        AddOrderWidget.resize(555, 358)
        AddOrderWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        AddOrderWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(AddOrderWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget_2 = QtGui.QWidget(AddOrderWidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(AddOrderWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.description = QtGui.QTextEdit(AddOrderWidget)
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout.addWidget(self.description, 1, 0, 1, 2)
        self.widget = QtGui.QWidget(AddOrderWidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.client = QtGui.QComboBox(self.widget)
        self.client.setObjectName(_fromUtf8("client"))
        self.gridLayout_2.addWidget(self.client, 0, 0, 1, 1)
        self.add_client_btn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_client_btn.sizePolicy().hasHeightForWidth())
        self.add_client_btn.setSizePolicy(sizePolicy)
        self.add_client_btn.setMinimumSize(QtCore.QSize(22, 22))
        self.add_client_btn.setMaximumSize(QtCore.QSize(22, 22))
        self.add_client_btn.setObjectName(_fromUtf8("add_client_btn"))
        self.gridLayout_2.addWidget(self.add_client_btn, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(313, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.device = QtGui.QLineEdit(self.widget)
        self.device.setObjectName(_fromUtf8("device"))
        self.gridLayout_2.addWidget(self.device, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.retranslateUi(AddOrderWidget)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddOrderWidget.close)
        QtCore.QMetaObject.connectSlotsByName(AddOrderWidget)

    def retranslateUi(self, AddOrderWidget):
        AddOrderWidget.setWindowTitle(QtGui.QApplication.translate("AddOrderWidget", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddOrderWidget", "Клиент", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddOrderWidget", "Что сломалось", None, QtGui.QApplication.UnicodeUTF8))
        self.description.setHtml(QtGui.QApplication.translate("AddOrderWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Описание проблемы</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.add_client_btn.setText(QtGui.QApplication.translate("AddOrderWidget", "+", None, QtGui.QApplication.UnicodeUTF8))

