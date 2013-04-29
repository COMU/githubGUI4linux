# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oauth.ui'
#
# Created: Thu Apr 25 16:18:48 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtWebKit
import sys
import oauth2 as oauth
import urllib, urllib2
import urlparse
from i18n import _
from common import CONSUMER_KEY, CONSUMER_SECRET, HOST


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):	
    
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

# OAuth icin gizli ve acik anahtarlarin kullanimasi icin bos stringler olsturuldu
        self.oauth_token = ''
        self.oauth_secret = ''

        self.loadUrl(QtCore.QUrl('http://github4linux.com/'))	# OAuth icin gizli ve acik key alirken main URL kismina girdigimiz kisim

    def loadUrl(self, url):
	# WebKit araciligi ile OAuth kullanarak kimlik kanitlamasi yapilmasi icin gerekenler
	view = QtWebKit.QWebView()
	view.connect(view, QtCore.SIGNAL('loadFinished(bool)'),self.webkit_navigation_callback)
	view.load(url)
   
    def webkit_navigation_callback(self, frame, request, action, *args):
        url = action.get_uri()
        if "github4linux" in url: # url icinde daha onceden girdigimiz adres icindeki isim ile karsilasiyorsa (url icin "http://github4linux.com/" demistik) yapilmasi gerekenler
            self.hide()

            oauth_verifier = url.split('oauth_verifier=')[-1]

            token = oauth.Token(self.oauth_token, self.oauth_secret)
            token.set_verifier(oauth_verifier)

            consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
            client = oauth.Client(consumer, token)
	    resp, content = client.request('https://%s/oauth' % HOST, 'POST')
            access_token = dict(urlparse.parse_qsl(content))

            ENAPI.set_access_token(access_token['oauth_token'])

        return False

    def get_oauth_url(self):
        consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        client = oauth.Client(consumer)

        # set http://github4linux/home as dummy callback url
        # we will catch this url with webkit events.
        resp, content = client.request('https://%s/oauth?oauth_callback=' % HOST + urllib.quote('http://en-linuxclipper/'), 'GET')

        data = dict(urlparse.parse_qsl(content))

        self.oauth_token = data['oauth_token']
        self.oauth_secret = data['oauth_token_secret']

        return 'http://%s/OAuth.action?oauth_token=' % HOST + urllib.quote(data['oauth_token'])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 20, 251, 211))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../Masaüstü/github-yeni proje/githubpy/github-logo.png")))
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
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 350, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
	self.uyariLabel = QtGui.QLabel(self.centralwidget)
        self.uyariLabel.setGeometry(QtCore.QRect(40, 320, 701, 17))
        self.uyariLabel.setObjectName(_fromUtf8("uyariLabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
	QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.getUserData)
        QtCore.QObject.connect(self.lineEdit,QtCore.SIGNAL("returnPressed()"),self.pushButton.animateClick)
	QtCore.QObject.connect(self.lineEdit_2,QtCore.SIGNAL("returnPressed()"),self.pushButton.animateClick)

	self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)	# girilen parolanin gorulmesini engellemek icin

	QtCore.QMetaObject.connectSlotsByName(MainWindow)

# kullanici tarafindan arayuzden girilen kullanici adi ve parolasinin alinip boyle bir kullanicinin var olup olmadiginin sorusturulmasi

    def getUserData(self):
	uName = str(ui.lineEdit.text())
	pWord = str(ui.lineEdit_2.text())
	try:
		userData = "Basic " + (uName + ":" + pWord).encode("base64").rstrip()

        	req = urllib2.Request('https://api.github.com/users/braitsch')

        	req.add_header('Accept', 'application/json')
        	req.add_header("Content-type", "application/x-www-form-urlencoded")

        	req.add_header('Authorization', userData)

        	res = urllib2.urlopen(req)
		print "authorization" 
		ui.lineEdit.clear()
		ui.lineEdit_2.clear()
	except:
		ui.uyariLabel.setText(u"internet baglantinizda ya da girdiginiz kullanici adi ve parolasinda hata bulunmaktadir. Kontrol ediniz!")
		ui.lineEdit.clear()
                ui.lineEdit_2.clear()
	
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
	self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Welcome To Github4Linux</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">connect to github</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Github username or e-mail:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Password:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "LOG IN", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "SKIP SETUP", None, QtGui.QApplication.UnicodeUTF8))


app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
