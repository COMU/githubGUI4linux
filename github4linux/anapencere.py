#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from linux_github_gui import FindLocalRepoWindow
from githubApplication  import UserPageWindow as DigerPencere

import sys


class DigerPencerem(QtGui.QDialog, DigerPencere):
        def __init__(self):
                QtGui.QDialog.__init__(self)
                self.setupUi(self)
class MainWindow(QtGui.QMainWindow, FindLocalRepoWindow):
        def __init__(self):
                QtGui.QMainWindow.__init__(self)
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
		print self.digerPencere.localRepoList
	        #self.digerPencere.repolistBox = QtGui.QTreeWidget(Dialog)
	        #self.digerPencere.repolistBox.setGeometry(QtCore.QRect(10,30,150,200))
        	#self.digerPencere.repolistBox.setHeaderLabels(["Repositorylist"])
        	#root = QtGui.QTreeWidgetItem(self.digerPencere.repolistBox, ["Repositories"])
        	#print self.localRepoList
		root = QtGui.QTreeWidgetItem(self.digerPencere.repolistBox, ["Repositories"]) 
        	for i in self.digerPencere.localRepoList:
            		repo = QtGui.QTreeWidgetItem(root,[i]) 
        	#print "listtttttttttt"
        	print self.digerPencere.localRepoList
        	#self.digerPencere.repolistBox.show()
 
app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
