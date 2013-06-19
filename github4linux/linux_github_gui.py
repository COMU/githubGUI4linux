# -*- coding: utf-8 -*-
#denemesatirideneme satirii
#deneme
# Form implementation generated from reading ui file 'repos.ui'
# Created: Wed Mar 13 13:02:39 2013
#      bmmplementation generated from reading ui file 'repos.ui': PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import commands
import sys
import glob
#from gui import *
from urllib import *
import json
import requests
from github import *
import git
from configobj import ConfigObj
import subprocess
from git import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

localRepoList = []
file_list = []
value_list = []
array_list = []
local_repo_user = []
value_local = []

class FindLocalRepoWindow(object):
    def setupUi(self,MainWindow):
	
	#QtGui.QMainWindow.__init__(self)	

	MainWindow.setObjectName(_fromUtf8("Adding Local Repos"))
        MainWindow.resize(800,600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
	self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 251, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 40, 241, 211))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("pictures/github-logo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))     
        self.label_2.show()
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 470, 111, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 470, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 150, 401, 151))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
	

	# program kuruldugunda, kullanicinin yerelinde otomatik olarak bir dizin olusturuluyor

        home = commands.getoutput('~/') # kullanicinin home dizinini buluruz.
        home_name = home.split(" ")
        home_name = home_name[2].split(":")
        home = home_name[0]

	print home

        direc = commands.getstatusoutput('mkdir '+home+'/GitHubLINUX') # GitHubLINUX isminde bir dizin olusur arka planda. eger bu dizin daha onceden varsa ayni dizinden bir daha olusturulmayacaktir.


        # .git uzantili dosyalari bulma islemi burada yapiliyor.
        # Eger dosya bulunuyorsa deponun ismini diziden cekip arayuzde gosteriyoruz.


	repos_name_array = []
	array = []
	#value = []
	for files in glob.iglob(home+"*/.git"):
		
		filename = files+"/config"
	#	config = ConfigObj(filename)
	#	local_url_value = config['remote "origin"']['url']
		file_list.append(filename)
        	repos_name = files.split('/')
        	repos_name_array.append(repos_name)
                
	#	value.append(local_url_value)	
	array_size = len(repos_name_array)
	for i in range (0,array_size):
        	array = repos_name_array[i]
		self.listWidget.addItem(array[3])
	        

        self.retranslateUi(MainWindow)
	
	#self.listWidget.itemActivated.connect(self.listWidget.currentItem())
	self.connect(self.listWidget, QtCore.SIGNAL("itemSelectionChanged()"), self.printItemText)
 		
#	QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenUserPageWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QMetaObject.connectSlotsByName(self)
    def printItemText(self):
	items = self.listWidget.selectedItems()
	
	for i in range(len(items)):
		localRepoList.append(str(self.listWidget.selectedItems()[i].text()))
                print localRepoList[0]	
                for i in range(0,len(file_list)):     
         	      value = file_list[i].split('/')
		      print value[3]	
		      if value[3] == localRepoList[0]:
						
		     	
                          config = ConfigObj(file_list[i])
        	          local_url_value = config['remote "origin"']['url']
	                  value_list.append(local_url_value)
        local = value_list[0].split('/')
	print "user="
        value_local.append(local[3])
	print value_local
	return localRepoList
			 		 
    def OpenUserPageWindow(self):
	

        self.new = UserPageWindow()
	self.close()
	self.new.show()
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Add Your Local Repository for githubgui4linux", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Find Local Repositories</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                                                           
	self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "ADD SELECTED", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "SKIP", None, QtGui.QApplication.UnicodeUTF8))
