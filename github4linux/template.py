#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from oauth_authentication import Ui_MainWindow
from linux_github_gui  import FindLocalRepoWindow as DigerPencere

import sys

class DigerPencerem(QtGui.QDialog, DigerPencere):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		#self.setupUi(self)
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		#self.setupUi(self)
		self.digerPencere = DigerPencerem()
	
	@QtCore.pyqtSignature("bool")
	def on_pushButton_clicked(self):
		self.digerPencere.exec_()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_()) 

