pyJasperClient
==============

A python client for the Jasper Report Server

Usage
==============

1. Get Jasper Server Version
	```
	import jasper
	j = jasper.JasperClient(host='jasperserver',port=8080,org='organization_1',username='jasperadmin',password='password')
	print j.get_version()
	```

2. Getting a report in pdf format

	```
	```



