from PyQt4 import QtCore, QtGui, QtWebKit
import sys
import oauth2 as oauth
import urllib, urllib2
import urlparse
from urlparse import urljoin
import requests
import getpass
import json
import time
import webbrowser
from common import client_id, client_secret, code
import subprocess


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

uName = []
class Ui_MainWindow(object):
	def setupUi(self,MainWindow):
		#QtGui.QMainWindow.__init__(self)

	

        	MainWindow.setObjectName(_fromUtf8("MainWindow"))
        	MainWindow.resize(800, 600)
        	self.centralwidget = QtGui.QWidget(MainWindow)
        	self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        	self.label = QtGui.QLabel(self.centralwidget)
        	#self.label.setGeometry(QtCore.QRect(540, 20, 251, 211))
        	self.label.setText(_fromUtf8(""))
        	self.label.setPixmap(QtGui.QPixmap(_fromUtf8("pictures/github-logo.png")))
        	self.label.setObjectName(_fromUtf8("label"))
        	self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        	self.lineEdit.setGeometry(QtCore.QRect(250, 220, 281, 27))
        	self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        	self.label_2 = QtGui.QLabel(self.centralwidget)
        	self.label_2.setGeometry(QtCore.QRect(30, 50, 351, 41))
        	self.label_2.setObjectName(_fromUtf8("label_2"))
        	self.label_3 = QtGui.QLabel(self.centralwidget)
        	self.label_3.setGeometry(QtCore.QRect(40, 130, 161, 31))
        	self.label_3.setObjectName(_fromUtf8("label_3"))
        	self.label_4 = QtGui.QLabel(self.centralwidget)
        	self.label_4.setGeometry(QtCore.QRect(40, 220, 191, 21))
        	self.label_4.setObjectName(_fromUtf8("label_4"))
        	self.label_5 = QtGui.QLabel(self.centralwidget)
        	self.label_5.setGeometry(QtCore.QRect(40, 270, 81, 21))
        	self.label_5.setObjectName(_fromUtf8("label_5"))
        	self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        	self.lineEdit_2.setGeometry(QtCore.QRect(250, 260, 281, 27))
        	self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        	self.pushButton = QtGui.QPushButton(self.centralwidget)
        	self.pushButton.setGeometry(QtCore.QRect(250, 350, 98, 27))
		icon = QtGui.QIcon()
        	icon.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/login.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        	self.pushButton.setIcon(icon)
        	self.pushButton.setObjectName(_fromUtf8("pushButton"))
        	self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        	self.pushButton_2.setGeometry(QtCore.QRect(380, 350, 98, 27))
        	self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		icon1 = QtGui.QIcon()
        	icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pictures/skip.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        	self.pushButton_2.setIcon(icon1)
        	self.uyariLabel = QtGui.QLabel(self.centralwidget)
        	self.uyariLabel.setGeometry(QtCore.QRect(40, 320, 701, 17))
        	self.uyariLabel.setObjectName(_fromUtf8("uyariLabel"))
        	self.setCentralWidget(self.centralwidget)
        	self.menubar = QtGui.QMenuBar(MainWindow)
        	self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        	self.menubar.setObjectName(_fromUtf8("menubar"))
        	self.setMenuBar(self.menubar)
        	self.statusbar = QtGui.QStatusBar(MainWindow)
        	self.statusbar.setObjectName(_fromUtf8("statusbar"))
		self.setStatusBar(self.statusbar)

        	self.retranslateUi(MainWindow)
        	QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.close)
        	QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.authentication)
        	QtCore.QObject.connect(self.lineEdit,QtCore.SIGNAL("returnPressed()"),self.pushButton.animateClick)
        	QtCore.QObject.connect(self.lineEdit_2,QtCore.SIGNAL("returnPressed()"),self.pushButton.animateClick)

        	self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)   # girilen parolanin gorulmesini engellemek icin

        	QtCore.QMetaObject.connectSlotsByName(MainWindow)


# kullanici tarafindan arayuzden girilen kullanici adi ve parolasinin alinip boyle bir kullanicinin var olup olmadiginin sorusturulmasi
		
	def authentication(self):
		flag = 1	
	        # kullanici adi ve parolasi alinarak token degeri elde ediliyor.
	        github_api = "https://api.github.com"
	        uName.append(str(self.lineEdit.text()))
	        pWord = str(self.lineEdit_2.text())
		
		try:
	                userData = "Basic " + (uName[0] + ":" + pWord).encode("base64").rstrip()
	
	                req = urllib2.Request('https://api.github.com/users/braitsch')
	
	                req.add_header('Accept', 'application/json')
	                req.add_header("Content-type", "application/x-www-form-urlencoded")
	
	                req.add_header('Authorization', userData)
	
	                res = urllib2.urlopen(req)
	                self.lineEdit.clear()
	                self.lineEdit_2.clear()
			self.uyariLabel.clear()
	        except:
	                self.uyariLabel.setText(u"internet baglantinizda ya da girdiginiz kullanici adi ve parolasinda hata bulunmaktadir. Kontrol ediniz!")
	               # self.lineEdit.clear()
	                self.lineEdit_2.clear()
			flag = 0

# github da her kullanici icin kendi hesaplarindaki applications kisminda github tarafindan uygulamaya izin verilir
		if flag == 1: 
		        note = "github4linux"
		        url = urljoin(github_api, 'authorizations')
		        payload = {}
		        if note:
		                payload['note'] = note
		        res = requests.post(
		                url,
		                auth = (uName[0], pWord),
		                data = json.dumps(payload),
		                )
			
		        j = json.loads(res.text)
			if res.status_code >= 400: 
        			msg = j.get('message', 'UNDEFINED ERROR (no error description from server)')
        			print 'ERROR: %s' % msg
        			return
			print "J: ",j
		        oauth_token = j['token'] # oauth token degeri elde ediliyor.
		        print "oauth token : ",oauth_token

	# istekte bulunabilecegimiz github oauth adreslerinin tamami
			request_token_url = "https://api.github.com"
			authorize_url = "https://github.com/login/oauth/authorize"
			redirect_uri = "https://github4linux.com/oauth/callback"
			access_token_url = "https://github.com/login/oauth/access_token"

	# uygulama icin tarayicidan acilmasi gereken adres otomatik olarak tarayicida gosteriliyor.		
			new = 2	
			url = "%s?client_id=%s&scope=user" % (authorize_url,client_id) 
			webbrowser.open(url,new=new)
			
		        #file = "/home/mehtap/githubGUI4linux/github4linux/linux_github_gui.py"
   			#subprocess.call(["python",file])		     
	
	                #url = "%soauth_token=%s" % (authorize_url,oauth_token) # bu kod calistigi zaman github hesabin baskasi tarafindan ele gecirildigini zannedip parolanin yenilenmesini istiyor ve sizi otomatik olarak github'in parola yenileme sayfasina gonderiyor.
                        #webbrowser.open(url,new=new)
   
				
		#	print "Go to the following link in your browser:"
		#	print "%s?client_id=%s&scope=repo&redirect_uri=%s" % (authorize_url,consumer_key, redirect_uri)       
	def name(self):
		return uName[0]		
	def retranslateUi(self,MainWindow):
       		 MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "githubGUI4linux", None, QtGui.QApplication.UnicodeUTF8))
       		 self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Welcome To Github4Linux</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
       		 self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">connect to github</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
       		 self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Github Username:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
       		 self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Password:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
       		 self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "LOG IN", None, QtGui.QApplication.UnicodeUTF8))
       		 self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "SKIP SETUP", None, QtGui.QApplication.UnicodeUTF8))


#app = QtGui.QApplication(sys.argv)
#ui = Ui_MainWindow()
#ui.show()
#sys.exit(app.exec_())
	
