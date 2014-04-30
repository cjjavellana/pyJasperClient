import unittest
import jasper
import os

class TestJasperClient(unittest.TestCase):
	"""
	Test harness for jasper client
	"""
	def setUp(self):
		pass
		#try:
		#	os.remove('report.pdf')
		#except:
		#	pass

	def test_getversion(self):
		j = jasper.JasperClient(host='192.168.56.60', port=8080, org='organization_1', username='jasperadmin', password='jasperadmin')
		print j.get_version()
		self.assertIsNotNone(j.get_version())
		
	def test_getreport(self):
		j = jasper.JasperClient(host='192.168.56.60', port=8080, org='organization_1', username='jasperadmin', password='jasperadmin')
		pdf = j.get_report(reportPath='public/DelvrReports/SalesOrder/SalesOrderInvoicejrxml',data='P_SALESORDER_ID=1');
		with open('report.pdf', 'wb') as code:
			code.write(pdf)
		self.assertIsNotNone(pdf)


if __name__ == '__main__':
    unittest.main()
