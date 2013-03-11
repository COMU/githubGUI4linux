# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repos.ui'
#
# Created: Fri Mar  8 13:53:42 2013
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
import git

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#github api
 
class github:
        def __init__(self, ui):
                self.ui = ui
        def user(self):
                gh = GitHub()
                edit = ui.lineEdit.text()

                user = gh.users(edit).get()
                return user


#ilk acilan pencere

class Ui_MainWindow(QtGui.QMainWindow):
    #def setupUi(self, MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(800, 600)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 80, 161, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 110, 281, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 150, 281, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 200, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 200, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 101, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 40, 221, 211))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("github-logo.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 191, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 160, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        
        
 
        self.retranslateUi(self)
	#self.github = github(self)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("selectionChanged()")), self.pushButton.click)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8("selectionChanged()")), self.pushButton.click)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.open_window)
        QtCore.QMetaObject.connectSlotsByName(self)

#ikinci ekrana gecis

    def open_window(self):
         self.close()
         self.new = Ui_MainWindow2()

         self.new.show()

 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">connect to github</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "LOG IN", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "SKIP SETUP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Welcome</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Github User Name or E-mail :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Password:", None, QtGui.QApplication.UnicodeUTF8))

#ikinci ekran

class Ui_MainWindow2(QtGui.QMainWindow):
    #def setupUi(self, MainWindow):
     def __init__(self):
        super(Ui_MainWindow2,self).__init__()
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(800, 600)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 251, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 40, 241, 211))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("github-logo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 470, 111, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 470, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 120, 151, 111))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))     
        #disarida tanimlanmis bir fonksiyon cagriliyor
        self.Ui_MainWindow = Ui_MainWindow()


        self.github = github(self)
        user = self.github.user()
        #user image'in gösterimi
        imageUrl = urllib2.urlopen(user.avatar_url)
        imageData = imageUrl.read()
        imageUrl.close()
        image = QtGui.QPixmap()
        image.loadFromData(imageData)
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(QtGui.QIcon(image))

        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(250, 210, 256, 192))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2")) 
        #listwidget'a user repos ekleniyor 
        liste = self.listWidget_2
        
        url = user.repos_url
        context = urllib.urlopen(url)
        context = context.read()
        context = json.loads(context)
        for repo in context:
            liste.addItem(repo['name'])
     #   self.connect(self.listWidget_2, SIGNAL("itemSelectionChanged()"), self.clone)
            
        
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QObject.connect(self.listWidget_2, QtCore.SIGNAL(_fromUtf8("itemSelectionChanged()")), self.clone)


        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QMetaObject.connectSlotsByName(self)
     def clone(self,item):
        print "hey"
        user = self.github.user()
        #items = self.listWidget.selectedItems()
        url = user.repos_url
        context = urllib.urlopen(url)
        context = context.read()
        context = json.loads(context)
        print "devam"
        for repo in context:
            print "sorun yok burada da"
            repo = repo['name']
            print "heeey gectin burayi da"
            #items = self.listWidget.selectedItems()
            print ":("
            #print items
           # for i in range(len(items)):
            #       print "dedevam"
            #clone_url = str(self.listWidget_2.selectedItems().text())
            selectItem = self.listWidget_2.currentItem().text()
            
            print selectItem
            if selectItem == repo:
                 
                  git.Git().clone(repo['clone_url'])   
                  print "clone yapildi"
            
     def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Find Local Repositories</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "ADD SELECTED", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "SKIP", None, QtGui.QApplication.UnicodeUTF8))


app = QtGui.QApplication(sys.argv)
ui = Ui_MainWindow()
ui.show()
sys.exit(app.exec_())

