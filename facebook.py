import urllib2
import urllib
import cookielib

fb_username = raw_input('Type email: ').replace('\n', '')
fb_password = raw_input('Type password: ').replace('\n', '')


def login(opener, login, password):
	login_data = urllib.urlencode({
		'email': login,
		'pass': password,
	})
	response = opener.open('https://www.facebook.com/login.php', login_data)
	return ''.join(response.readlines())


cj = cookielib.CookieJar()

opener = urllib2.build_opener(
	urllib2.HTTPRedirectHandler(),
	urllib2.HTTPHandler(debuglevel=0),
	urllib2.HTTPHandler(debuglevel=0),
	urllib2.HTTPCookieProcessor(cj)
)

# This basically fakes the HTTP header to think that the request is coming from a browser, not an automated bot
opener.addheaders = [
	('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
					'Windows NT 5.2; .NET CLR 1.1.4322)'))
]


# Send the login thing twice since you need the cookie to be set up first and then login
login(opener, fb_username, fb_password) 
print login(opener, fb_username, fb_password)
