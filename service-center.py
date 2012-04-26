# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import gui.LoginWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    window = gui.LoginWindow.LoginWindow()
    window.show()
    sys.exit(app.exec_())