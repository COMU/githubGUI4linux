# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gitgui.ui'
#
# Created: Tue Mar 19 23:56:11 2013
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
class github:
        def __init__(self, ui):
                self.ui = ui
        def user(self):
                gh = GitHub()
                edit_name = 'nyucel'
                user = gh.users(edit_name).get()
                print "user",user
                return user


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(800, 600)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 80, 171, 441))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.listWidget = QtGui.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(10, 280, 41, 31))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.resize(30,30)       
        self.github = github(self)
        user = self.github.user()
        #user image'in gösterimi
        print user
        imageUrl = urllib2.urlopen(user.avatar_url)
        imageData = imageUrl.read()
        imageUrl.close()
        image = QtGui.QPixmap()
        image.loadFromData(imageData)
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(QtGui.QIcon(image))

        self.listWidget_2 = QtGui.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 360, 41, 31))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.listWidget_2.resize(30,30)
        self.github = github(self)
        user = self.github.user()
        #user image'in gösterimi
        url = user.organizations_url
        context = urllib.urlopen(url)
        context = context.read()
        context = json.loads(context)
        for organization in context:
          imageUrl = urllib2.urlopen(organization['avatar_url'])
          imageData = imageUrl.read()
          imageUrl.close()
          image = QtGui.QPixmap()
          image.loadFromData(imageData)
          item = QtGui.QListWidgetItem(self.listWidget_2)
          item.setIcon(QtGui.QIcon(image))
        

        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 280, 97, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 370, 97, 24))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 201))     
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("github-logo.png")))


        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 320, 97, 24))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(170, 80, 461, 441))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))

        self.github = github(self)
        user = self.github.user()


        self.listWidget_3 = QtGui.QListWidget(self.frame_2)
        self.listWidget_3.setGeometry(QtCore.QRect(50, 120, 151, 111))
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.listWidget_3.resize(200,200)

        self.listWidget_4 = QtGui.QListWidget(self.frame_2)
        self.listWidget_4.setGeometry(QtCore.QRect(50, 120, 151, 111))
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        self.listWidget_4.resize(200,200)

        #liste = self.listWidget_3
        self.pushButton_4 = QtGui.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(200,280,70, 24))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))



  

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
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.repos_list)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.organizations_list)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clone_organization_repo)
    def clone_organization_repo(self):
        user = self.github.user()
        #items = self.listWidget.selectedItems()
        url = user.organizations_url
        context = urllib.urlopen(url)
        context = context.read()
        context = json.loads(context)
        for organization in context:
            url_repo = organization['repos_url']
            context_repo = urllib.urlopen(url_repo)
            context_repo = context_repo.read()
            context_repo = json.loads(context_repo)
            for name in context_repo:
                    repo_name = name['name']

                    selectItem = self.listWidget_4.currentItem().text()

                    print selectItem
                    if selectItem == repo_name:
                         #print repo['clone_url']

                         git.Git().clone(name['clone_url'])

                         print "clone yapildi"

    def organizations_list(self):
        self.github = github(self)
        user = self.github.user()
        liste = self.listWidget_4

        url = user.organizations_url
        context = urllib.urlopen(url)
        context = context.read()
        context = json.loads(context)
        for organization in context:
            url_repo = organization['repos_url']
            context_repo = urllib.urlopen(url_repo)
            context_repo = context_repo.read()
            context_repo = json.loads(context_repo)
            for repo_name in context_repo:
                 liste.addItem(repo_name['name'])
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setGeometry(QtCore.QRect(300,280,90, 24))


        print organization['repos_url']
        print "bittiiiii"

        print "merhaba"
    def repos_list(self):
        
        self.github = github(self)
        user = self.github.user()
        liste = self.listWidget_3

        url = user.repos_url
        context = urllib.urlopen(url)
        context = context.read()
        context = json.loads(context)
        for repo in context:
            liste.addItem(repo['name'])
            print repo['name']
        print "bittiiiii"    
    def label_name(self,i):
        self.label.setText(_fromUtf8(i))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "REPOS", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "ORGANİZATİON", None, QtGui.QApplication.UnicodeUTF8))
        #self.label_2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "LOCAL REPOS", None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "clone", None, QtGui.QApplication.UnicodeUTF8))


app = QtGui.QApplication(sys.argv)
ui = Ui_MainWindow()
ui.show()
sys.exit(app.exec_())
                           
