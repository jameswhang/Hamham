import urllib2
import HTMLParser
import mechanize
import cookielib
from bs4 import BeautifulSoup
import requests

################ SORRY IGNORE THIS PLEASE ############################

### Browser
##br = mechanize.Browser()
##
### Cookie Jar
##cj = cookielib.CookieJar()
##br.set_cookiejar(cj)
##
### Browser options
##br.set_handle_equiv(True)
##br.set_handle_redirect(True)
##br.set_handle_referer(True)
##br.set_handle_robots(False)
##br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
##br.addheaders = [('User-agent', 'Chrome')]
##
### Open Login Page
##br.open('https://hiring.monster.com/login.aspx')
##br.select_form(nr=0)
##br.set_all_readonly(False)
##
### Input Login
##user = raw_input('Username/Email: ')
##password = raw_input('Password: ')    
##br.form['user'] = str(user)
##br.form['password'] = str(password)
##br.submit()

######################################################################

s = requests.session()
USER = raw_input('Username/Email: ')
PASSWORD = raw_input('Password: ')
login_data = dict(user = USER, password = PASSWORD)
s.post('https://hiring.monster.com/login.aspx', data = login_data)

### Get url
##def changeToURLParam(some_str):
##    return some_str.replace('+', '%').replace(' ', '+').replace('#', '%23')
##while True:
####    keywords = raw_input('keywords: ')
####    zipcode = raw_input('zip code: ')
####    radius = raw_input('radius: ')
##
##    keywords = '"linux" and "system administration" or "dba" and "powershell"'
##    zipcode = 98052
##    radius = raw_input('radius: ')
##    
##    url = 'http://hiring.monster.com/jcm/resumesearch/searchresults.aspx?mdatemaxage=20160&rb=1&tsni=0&clv=&tcc=&q=' + changeToURLParam(keywords) + '&rpcr=' + str(zipcode) + '-' + str(radius) + '&co=US&zipcode=' + str(zipcode) + '&radius' + str(radius) + '&rlid=316#s=grid'
##    req1 = urllib2.Request(url)
##    req1.add_header('cookie', cookie)
##    response = urllib2.urlopen(req1)   
##    
##    soup = BeautifulSoup(response.read())
##    print(soup.prettify())
##    
