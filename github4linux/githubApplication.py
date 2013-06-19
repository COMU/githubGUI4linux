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

#localRepoList = []
#file_list = []
#value_list = []
#array_list = []
#local_repo_user = []
#value_local = []


#class github:
#        def __init__(self, ui):
#                self.ui = ui
                #app = QtGui.QApplication(sys.argv)
                #window = QtGui.QMainWindow()


#        def user(self):
#                gh = GitHub()
                #edit_name ='nyucel'


class UserPageWindow(object):
    def setupUi(self,Dialog):
	#localRepoList = []
	#file_list = []
	#value_list = []
	#array_list = []
	#local_repo_user = []
	#value_local = []
	#super(UserPageWindow,self).__init__()
        #QtGui.QMainWindow.__init__(self)
        Dialog.setObjectName(_fromUtf8("Github4Linux"))
        Dialog.resize(800,600)
        #self.centralwidget = QtGui.QWidget(MainWindow)
        #self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
	#self.local_repo_user = []
	#self.value_local = []
	self.localRepoList = []
	self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(610, 40,350, 211))
        self.label_2.setText(_fromUtf8(""))
        #self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("picture/github-logo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.show()
  	#self.clone_url = UserPageWindow(QtGui.QMainWindow) 
	#githubtan depolar
	gh = GitHub()
	user = gh.users('nyucel').get()
	#self.github = github(self)
        #user = self.github.user()
        repo_url = user.repos_url
        context = urllib.urlopen(repo_url)
        context = context.read()
        context = json.loads(context)
	
	organization_url = user.organizations_url
	context2 = urllib.urlopen(organization_url)
        context2 = context2.read()
        context2 = json.loads(context2)
 
	self.organizationlistBox = QtGui.QTreeWidget(Dialog)
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

      	
        self.repolistBox = QtGui.QTreeWidget(Dialog)
	self.repolistBox.setGeometry(QtCore.QRect(10,30,150,200))
	self.repolistBox.setHeaderLabels(["Repositorylist"])
        #root = QtGui.QTreeWidgetItem(self.repolistBox, ["Repositories"])
	#print self.localRepoList 
	#for i in self.localRepoList:
	 #   repo = QtGui.QTreeWidgetItem(root,[i])
	#print "listtttttttttt"
	#print self.localRepoList 
	self.repolistBox.show()
        
	self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 30,30, 20))
        self.pushButton.setObjectName(_fromUtf8("clone"))
        self.pushButton.hide()
        self.tabWidget = QtGui.QTabWidget(Dialog)
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
        #self.setCentralWidget(self.centralwidget)
        #self.menubar = QtGui.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        #self.menubar.setObjectName(_fromUtf8("menubar"))
        #self.setMenuBar(self.menubar)
        #self.statusbar = QtGui.QStatusBar(MainWindow)
        #self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #self.setStatusBar(self.statusbar)
	
	self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(610, 40, 241, 211))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("picture/github-logo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.show() 

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
       
	self.repolistBox.itemSelectionChanged.connect(self.displayItem)
        self.repolistBox.itemSelectionChanged.connect(self.repoItem_chosen)
	self.organizationlistBox.itemSelectionChanged.connect(self.organizationItem_chosen)


	
    def displayItem(self):
                        colmIndex=0
                        print self.repolistBox.currentItem().text(colmIndex)
    def organizationItem_chosen(self):
	colmIndex = 0
	text = self.organizationlistBox.currentItem().text(colmIndex)
	print text

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/repo.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.clear()
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab,icon1, _fromUtf8("REPO"))
        self.label_2 = QtGui.QLabel()
        self.label_2.setGeometry(QtCore.QRect(610, 40, 350, 211))
        self.label_2.setText(_fromUtf8(""))

        self.label_2.show() 
        x = 361
	x1 = 370
        y1 = 20
	y2 = 60	
	a = 30
	px = 30
        py = 30
        pz = 20
	self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(10,a,x,y1))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton= QtGui.QPushButton(self.frame_2)
	self.pushButton.move(250,0)
        self.pushButton.setText("clone")

        self.label2 = QtGui.QLabel(self.frame_2)
        self.label2.setText(text)
        self.label2.move(50,0)
        self.frame_2.show()
        self.label2.show()
        self.pushButton.show()
	QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clone)

    def goster(self):
	print "merhaba" 	
    def clone(self):    
       colmIndex = 0
       #self.github = github(self)	
       #user = self.github.user()
       gh = GitHub()
       user = gh.users('nyucel').get()
			
       git.Git().clone("https://github.com/"+user.login+"/"+self.organizationlistBox.currentItem().text(colmIndex)+".git")
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
        self.label_2 = QtGui.QLabel(Dialog)
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
	y3 = 20
	b = 30
        self.github = github(self)
        print self.github.user()
	#yerel repo uncommit files
	repo = git.Repo('/home/mehtap/githubGUI4linux/github4linux/')
	
        for i in repo.untracked_files:
                 self.frame_2 = QtGui.QFrame(self.tab2)
                 self.frame_2.setGeometry(QtCore.QRect(10,b,x,y3))
                 self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
                 self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
                 self.frame_2.setObjectName(_fromUtf8("frame_2"))
                 self.pushButton= QtGui.QPushButton(self.frame_2)
                 self.pushButton.move(250,0)
                 self.pushButton.setText("commit")

                 self.label2 = QtGui.QLabel(self.frame_2)
                 self.label2.setText(i)
                 self.label2.move(50,0)
		 self.frame_2.show()
                 self.label2.show()
                 self.pushButton.show()
                 y3 = y3 +1
                 b = b+30
	
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

	 		 
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GithubGUI4linux", None, QtGui.QApplication.UnicodeUTF8))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
	self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "look repo content", None, QtGui.QApplication.UnicodeUTF8))

