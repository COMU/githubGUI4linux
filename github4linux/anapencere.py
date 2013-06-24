#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from linux_github_gui import FindLocalRepoWindow
from githubApplication  import UserPageWindow as DigerPencere
from oauth_authentication import Ui_MainWindow
from github import *
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
		#self.digerPencere.edit_name = self.lineEdit.text()
		self.connect(self.listWidget, QtCore.SIGNAL("itemSelectionChanged()"), self.BackText)  
		self.digerPencere.repolistBox.itemSelectionChanged.connect(self.repoItem_chosen)      	   	     	
        @QtCore.pyqtSignature("bool")
        def on_pushButton_clicked(self):
		self.close()
		
                self.digerPencere.exec_()
	def repoItem_chosen(self):
        	colmIndex = 0
        	text = self.digerPencere.repolistBox.currentItem().text(colmIndex)

       		 #icon1 = QtGui.QIcon()
       		 #icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/history.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
       		 #icon2 = QtGui.QIcon()
       		 #icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/changes.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
       		 #icon3 = QtGui.QIcon()
       		 #icon3.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/branches.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		 self.digerPencere.tabWidget.clear()
	         self.digerPencere.tab = QtGui.QWidget()
       		 self.digerPencere.tab.setObjectName(_fromUtf8("tab"))

       		 self.digerPencere.tab2 = QtGui.QWidget()
       		 self.digerPencere.tab2.setObjectName(_fromUtf8("tab2"))
       		 self.digerPencere.tab3 = QtGui.QWidget()
        	 self.digerPencere.tab3.setObjectName(_fromUtf8("tab3"))
       		 self.digerPencere.tabWidget.addTab(self.digerPencere.tab, _fromUtf8("HISTORY"))
       		 self.digerPencere.tabWidget.addTab(self.digerPencere.tab2,_fromUtf8("CHANGES"))
       		 self.digerPencere.tabWidget.addTab(self.tab3,_fromUtf8("BRANCHES"))
       		 self.digerPencere.label_2 = QtGui.QLabel(Dialog)
       		 self.digerPencere.label_2.setGeometry(QtCore.QRect(510, 40, 241, 211))
       		 self.digerPencere.label_2.setText(_fromUtf8(""))
       		 self.digerPencere.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("pictures/github-logo.png")))
       		 self.digerPencere.label_2.setObjectName(_fromUtf8("label_2"))
       		 self.digerPencere.label_2.show()
		 x = 361
	         x1 = 370
       		 y1 = 20
       		 y2 = 60
       		 a = 30
       		 y3 = 20
       		 b = 30
 
 	         #yerel repo uncommit files
       		 repo = git.Repo('/home/mehtap/githubGUI4linux/github4linux/')

       		 for i in repo.untracked_files:
                	 self.digerPencere.frame_2 = QtGui.QFrame(self.tab2)
                   	 self.digerPencere.frame_2.setGeometry(QtCore.QRect(10,b,x,y3))
                 	 self.digerPencere.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
                 	 self.digerPencere.frame_2.setFrameShadow(QtGui.QFrame.Raised)

	def BackText(self):
		self.nesne = MainWindow()
		self.digerPencere.edit_name = self.nesne.lineEdit.text()	
		gh = GitHub()
	        user = gh.users(self.digerPencere.edit_name).get()
        	
        	repo_url = user.repos_url
        	context = urllib.urlopen(repo_url)
       		context = context.read()
        	context = json.loads(context)

        	organization_url = user.organizations_url
        	context2 = urllib.urlopen(organization_url)
        	context2 = context2.read()
        	context2 = json.loads(context2)

		print "merak ettigim isim"	
                print self.digerPencere.edit_name  
		root = QtGui.QTreeWidgetItem(self.digerPencere.organizationlistBox, ["Organizations"])
	        #print type(root)

        	for organization_text in context2:
             		organization = QtGui.QTreeWidgetItem(root, [organization_text['login']])
        	root2 = QtGui.QTreeWidgetItem(self.digerPencere.organizationlistBox, ["Repositories"])
        	#print type(root2)
        	repo_url = user.repos_url
        	context = urllib.urlopen(repo_url)
        	context = context.read()
        	context = json.loads(context)
        	for repo_text in context:
             		repo = QtGui.QTreeWidgetItem(root2, [repo_text['name']])

            

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
		#gh = GitHub()
		#name = self.lineEdit.text()
		#user = gh.users(name).get()
	        #self.pencere.digerPencere.edit_name = self.lineEdit.text()
		#print self.pencere.digerPencere.edit_name		
                self.pencere.exec_()
	 
app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
