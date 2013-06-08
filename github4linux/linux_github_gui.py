# -*- coding: utf-8 -*-

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
class FindLocalRepoWindow(QtGui.QMainWindow):
    def __init__(self):
	QtGui.QMainWindow.__init__(self)
	self.setObjectName(_fromUtf8("Adding Local Repos"))
        self.resize(800,600)
        self.centralwidget = QtGui.QWidget(self)
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
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
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
	        

        self.retranslateUi(self)
	
	#self.listWidget.itemActivated.connect(self.listWidget.currentItem())
	self.connect(self.listWidget, QtCore.SIGNAL("itemSelectionChanged()"), self.printItemText)
 		
	QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenUserPageWindow)
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

	print localRepoList		 		 
    def OpenUserPageWindow(self):
	

        self.new = UserPageWindow()
	self.close()
	self.new.show()
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Add Your Local Repository for githubgui4linux", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Find Local Repositories</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
                                                           
	self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "ADD SELECTED", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "SKIP", None, QtGui.QApplication.UnicodeUTF8))
class github:
	def __init__(self, ui):
                self.ui = ui
        def user(self):
                gh = GitHub()
                edit_name = 'nyucel'
                user = gh.users(edit_name).get()
                return user

class UserPageWindow(QtGui.QMainWindow):
    def __init__(self):
	super(UserPageWindow,self).__init__()
        #QtGui.QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("Github4Linux"))
        self.resize(800,600)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 40,350, 211))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("picture/github-logo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.show()
  
	#githubtan depolar
	self.github = github(self)
        user = self.github.user()
        repo_url = user.repos_url
        context = urllib.urlopen(repo_url)
        context = context.read()
        context = json.loads(context)
	
	organization_url = user.organizations_url
	context2 = urllib.urlopen(organization_url)
        context2 = context2.read()
        context2 = json.loads(context2)
 
	self.organizationlistBox = QtGui.QTreeWidget(self.centralwidget)
	self.organizationlistBox.setGeometry(QtCore.QRect(10,250,150,240))
        self.organizationlistBox.setHeaderLabels(["Organizationlist"])
        root = QtGui.QTreeWidgetItem(self.organizationlistBox, ["Organizations"])
	#print type(root)

        for organization_text in context2:
             organization = QtGui.QTreeWidgetItem(root, [organization_text['login']])
	root2 = QtGui.QTreeWidgetItem(self.organizationlistBox, ["Repositories"])
	#print type(root2)
	repo_url = user.repos_url
        context = urllib.urlopen(repo_url)
        context = context.read()
        context = json.loads(context)
	for repo_text in context:
             repo = QtGui.QTreeWidgetItem(root2, [repo_text['name']])

        self.organizationlistBox.show()

      	
        self.repolistBox = QtGui.QTreeWidget(self.centralwidget)
	self.repolistBox.setGeometry(QtCore.QRect(10,30,150,200))
	self.repolistBox.setHeaderLabels(["Repositorylist"])
        root = QtGui.QTreeWidgetItem(self.repolistBox, ["Repositories"])
        for i in localRepoList:
	    repo = QtGui.QTreeWidgetItem(root,[i])	     
	self.repolistBox.show()
        
	self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 30,30, 20))
        self.pushButton.setObjectName(_fromUtf8("clone"))
        self.pushButton.hide()
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(160, 30, 441, 451))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        icon1 = QtGui.QIcon()
        
	
 	icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/history.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        

        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/changes.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        

        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/branches.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
	    
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
	self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))

        
        self.tabWidget.addTab(self.tab,icon1, _fromUtf8("HISTORY"))
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
	
	self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 40, 241, 211))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("picture/github-logo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.show() 

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
       
	self.repolistBox.itemSelectionChanged.connect(self.displayItem)
        self.repolistBox.itemSelectionChanged.connect(self.repoItem_chosen)
	self.organizationlistBox.itemSelectionChanged.connect(self.organizationItem_chosen)
	#QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clone(clone_url))


	
    def displayItem(self):
                        colmIndex=0
                        print self.repolistBox.currentItem().text(colmIndex)
    def organizationItem_chosen(self):
	colmIndex = 0
	text = self.organizationlistBox.currentItem().text(colmIndex)
	

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/repo.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.clear()
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab,icon1, _fromUtf8("REPO"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 40, 350, 211))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("pictures/github-logo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.show() 
        x = 361
	x1 = 370
        y1 = 20
	y2 = 60	
	a = 30
	px = 30
        py = 30
        pz = 20

        self.github = github(self)
        user = self.github.user()
        print type(user.login)
	
        if self.organizationlistBox.topLevelItem(1).text(colmIndex) :
	     self.github = github(self)
             user = self.github.user()
             print type(user.login)
	     repo_url = user.repos_url
             context = urllib.urlopen(repo_url)
             context = context.read()
             context = json.loads(context)
             for repo_text in context:
            # event_url = "https://api.github.com/repos/"+str(user.login)+"/"+str(text)
                  text2 = repo_text['name']	
	          clone_url = "https://github.com/"+user.login+"/"+str(text2)+".git"

                  self.addlabel2(x,x1,y1,y2,a,text2,px,py,pz,clone_url)
	          y1 = y1+1
		  y2 = y2+1
		  a = a+30	               
                  px = px +1
		  py = py+1
		  pz = pz +40		
    def addlabel2(self,x,x1,y1,y2,a,text2,px,py,pz,clone_url):

        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(10,a,x,y1))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton= QtGui.QPushButton(self.frame_2)

        #self.pushButton.setGeometry(QtCore.QRect(40,px,py,pz))
        self.pushButton.move(250,0)
        self.pushButton.setText("Look Content")
	QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clone(clone_url))

        self.label2 = QtGui.QLabel(self.frame_2)
        #self.label2.setGeometry(QtCore.QRect(20,80,370,y2 )) 
        self.label2.setText(text2)
        self.label2.move(50,0)
        self.frame_2.show()
        self.label2.show()
        self.pushButton.show()
	
    

        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clone(clone_url))
    def goster(self):
	print "merhaba" 	
    def clone(self,clone_url):    
       #clone_url = "https://github.com/"+user.login+"/"+str(text)+".git" 
	
	
       git.Git().clone(clone_url)
       print "clonelandi"          
    def repoItem_chosen(self):
	colmIndex = 0
	text = self.repolistBox.currentItem().text(colmIndex)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/history.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
	icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/changes.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
	icon3.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/branches.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.tabWidget.clear()
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))

        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))
        self.tabWidget.addTab(self.tab,icon1, _fromUtf8("HISTORY"))
        self.tabWidget.addTab(self.tab2,icon2,_fromUtf8("CHANGES"))
        self.tabWidget.addTab(self.tab3,icon3,_fromUtf8("BRANCHES"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 40, 241, 211))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("pictures/github-logo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.show() 
        x = 361
	x1 = 370
        y1 = 20
	y2 = 60	
	a = 30
        self.github = github(self)
        print self.github.user()
	user = value_local[0]
	print "hey"
        print user
        event_url = "https://api.github.com/repos/"+user+"/"+str(text)+"/events" 
	print event_url
	#event_url ="https://api.github.com/repos/nyucel/learnyouahaskell/events"   
        #print event_url
	event_icerik = urllib.urlopen(event_url)
	#print event_icerik
	event_icerik = event_icerik.read()
	event_icerik = json.loads(event_icerik)
	
        
	#self.label.setText(text)
	for event in event_icerik:
          
	   
	  for k in event:
	       
	    if k=='payload':
		  
               if 'commits' in event[k].keys():
                            			
		#if 'message' in event[k]['commits']:
	            for c in event[k]['commits']:
				text2 = c['message']
				
				url = c['url']	
				url_icerik = urllib.urlopen(url)
				url_icerik = url_icerik.read()
			        url_icerik = json.loads(url_icerik)
			        picture = url_icerik['author']['avatar_url']
				self.addlabel(y1,y2,text2,x,a,x1,picture)
			 	                    
           			y1 = y1 +1
				y2 = y2 +1
          		  	a = a+30
                                          			
       

              				
       
    		
    def addlabel(self,y1,y2,text2,x,a,x1,picture):   
        	
        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(10,a,x,y1))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        #self.pushButton= QtGui.QPushButton(self.tab)

	#self.pushButton.setGeometry(QtCore.QRect(370,30,30,20))
	#self.pushButton.setObjectName(_fromUtf8("pushButton"))
	self.label2 = QtGui.QLabel(self.frame_2)
        #self.label2.setGeometry(QtCore.QRect(20,80,370,y2 )) 
	self.label2.setText(text2)

	self.listWidget = QtGui.QListWidget(self.frame_2)
        #self.listWidget.setGeometry(QtCore.QRect(10, 360, 41, 31))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.resize(30,20)

	imageUrl = urllib2.urlopen(picture)
        imageData = imageUrl.read()
        imageUrl.close()
        image = QtGui.QPixmap()
        image.loadFromData(imageData)
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(QtGui.QIcon(image))

        self.listWidget2 = QtGui.QListWidget(self.frame_2)
        #self.listWidget.setGeometry(QtCore.QRect(10, 360, 41, 31))
        self.listWidget2.setObjectName(_fromUtf8("listWidget2"))
        self.listWidget2.resize(30,20)

        
        
        image2 = QtGui.QPixmap()
        image2.loadFromData("ok.gif")
        item = QtGui.QListWidgetItem(self.listWidget2)
        item.setIcon(QtGui.QIcon(image2))
        self.listWidget2.setGeometry(QtCore.QRect(10, 30, 360, 20))

#       self.label4 = QtGui.QLabel(self.frame_2)
#	pixmap = QtGui.QPixmap("ok.jpg")
#	self.label4.setPixmap(pixmap)
#       self.label4.move(80,0) 
	self.label2.move(50,0)
	self.frame_2.show()
	self.label2.show()
        #self.pushButton.show()
#       self.label4.show()
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GithubGUI4linux", None, QtGui.QApplication.UnicodeUTF8))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
	self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "look repo content", None, QtGui.QApplication.UnicodeUTF8))

app = QtGui.QApplication(sys.argv)
window = FindLocalRepoWindow()
window.show()
sys.exit(app.exec_())
