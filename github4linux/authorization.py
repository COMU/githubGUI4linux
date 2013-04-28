import urllib2 
#from github4linux import *

def getUserData():
        uName = 'kullanicininadi'
        pWord = 'parola'

	
	userData = "Basic " + (uName + ":" + pWord).encode("base64").rstrip()
	
	req = urllib2.Request('https://api.github.com/users/braitsch')
	
	req.add_header('Accept', 'application/json')
	req.add_header("Content-type", "application/x-www-form-urlencoded")
	
	req.add_header('Authorization', userData)
	
	res = urllib2.urlopen(req)

        print "authorization"

getUserData()
