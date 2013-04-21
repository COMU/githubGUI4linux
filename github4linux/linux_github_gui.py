# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Apr 19 13:00:19 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from github import *
from StringIO import StringIO
import Image
import urllib2
from PIL import Image
import requests
from StringIO import StringIO
import urllib, cStringIO
from urllib import *
import json

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class github:
	def __init__(self, ui):
                self.ui = ui
        def user(self):
                gh = GitHub()
                edit_name = 'nyucel'
                user = gh.users(edit_name).get()
                return user

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("MainWindow"))

       
        self.resize(800, 600)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 30, 151, 451))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.comboBox = QtGui.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 121, 24))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))   
	#githubtan depolar
	self.github = github(self)
        user = self.github.user()
        url = user.repos_url
        context = urllib.urlopen(url)
        context = context.read()
        context = json.loads(context)
        
	self.comboBox.clear()
        self.comboBox.addItem("Repository")
        for text in context:
    		self.comboBox.addItem(text['name'])


        self.comboBox_2 = QtGui.QComboBox(self.frame_3)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 100, 121, 24))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))

        	
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(160, 30, 441, 451))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        icon1 = QtGui.QIcon()
        

 	icon1.addPixmap(QtGui.QPixmap(_fromUtf8("/home/mehtap/BASLA/history.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        

        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("/home/mehtap/BASLA/changes.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        

        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("/home/mehtap/BASLA/branch.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
	self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))

	
        self.tabWidget.addTab(self.tab,icon1, _fromUtf8("HıSTORY"))
        self.tabWidget.addTab(self.tab2,icon2,_fromUtf8("CHANGES"))
	self.tabWidget.addTab(self.tab3,icon3, _fromUtf8("BRANCHES"))
        
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 201))


        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
	
	
	self.connect(self.comboBox, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)
    def combo_chosen(self,text):
	self.label.setText(text)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))


app = QtGui.QApplication(sys.argv)
ui = Ui_MainWindow()
ui.show()
sys.exit(app.exec_())


