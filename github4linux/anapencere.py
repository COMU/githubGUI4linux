#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from linux_github_gui import FindLocalRepoWindow
from githubApplication  import UserPageWindow as DigerPencere
from oauth_authentication import Ui_MainWindow

import sys


class DigerPencerem(QtGui.QDialog, DigerPencere):
        def __init__(self):
                QtGui.QDialog.__init__(self)
                self.setupUi(self)
class Pencere(QtGui.QDialog, FindLocalRepoWindow):
        def __init__(self):
                QtGui.QDialog.__init__(self)
		self.setupUi(self)
                self.digerPencere = DigerPencerem()
		self.connect(self.listWidget, QtCore.SIGNAL("itemSelectionChanged()"), self.BackText)        	   	     	
        @QtCore.pyqtSignature("bool")
        def on_pushButton_clicked(self):
		self.close()
                self.digerPencere.exec_()
	def BackText(self):
		print self.listWidget.currentItem().text()
        	self.digerPencere.localRepoList.append(self.listWidget.currentItem().text())
		root = QtGui.QTreeWidgetItem(self.digerPencere.repolistBox, ["Repositories"]) 
        	for i in self.digerPencere.localRepoList:
            		repo = QtGui.QTreeWidgetItem(root,[i]) 
        	print self.digerPencere.localRepoList
class MainWindow(QtGui.QMainWindow,Ui_MainWindow):
	def __init__(self):
                QtGui.QMainWindow.__init__(self)
                self.setupUi(self)
		self.pencere = Pencere()
	@QtCore.pyqtSignature("bool")
        def on_pushButton_clicked(self):
                self.close()
                self.pencere.exec_()
	 
app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
