
import urllib2
import base64

class JasperClient(object):
	"""
	A python client for interacting with Jasper Report Server
	"""

	def __init__(self, protocol='http',host='jasperhost',port=80,org=None,username=None,password=None):
		self.protocol=protocol
		self.host=host
		self.port=port
		self.org=org
		self.username=username
		self.password=password
		self.jasperUrl = self.protocol + '://' + self.host + ':' + str(self.port) + '/jasperserver-pro'


	def get_version(self,format='application/json'):
		"""
		Returns the Jasper Report Server version. 

		Please refer to section 1.3 of 
		http://community-static.jaspersoft.com/sites/default/files/docs/jasperreports-server-web-services-guide_1.pdf
		"""
		url = self.jasperUrl + '/rest_v2/serverInfo'
		print '%s' % (url)
		req = urllib2.Request(url)
		req.add_header('accept', format)
		resp = urllib2.urlopen(req)
		return resp.read()

	def get_report(self, reportPath=None, format='pdf', data=None):
		"""
		Generates a report 

		Please refer to section 3.2 of 
		http://community-static.jaspersoft.com/sites/default/files/docs/jasperreports-server-web-services-guide_1.pdf
		"""

		url = self.jasperUrl + '/rest_v2/reports/' + reportPath + "." + format + '?' + data

		#if we have an organization
		if self.org:
			print u'username: %s, org: %s, password: %s' % (self.username, self.org, self.password)
			auth = base64.b64encode(self.username + '|' + self.org + ':' + self.password)
		else:
			print u'username: %s, password: %s' % (self.username, self.password)
			auth = base64.b64encode(self.username + ':' + self.password)

		print u'Auth: %s' % (auth)

		req = urllib2.Request(url)
		req.add_header('Authorization', 'Basic ' + auth)

		f = urllib2.urlopen(req)
		return f.read()

