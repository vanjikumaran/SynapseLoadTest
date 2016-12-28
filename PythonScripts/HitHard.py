import hashlib
import os
import sys
import xml.dom.minidom as mini
import http.client

import threading
import datetime


numberOfconcurrency=200

sampleSoapMessage = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Header/><soapenv:Body><tests><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test><test>vfs_{0}</test></tests></soapenv:Body></soapenv:Envelope>"""

        
class ThreadClass(threading.Thread):
	def run(self):
		for i in range(1001, 1501):
			print(i)
			headers = {"Content-Type": "application/xml","SOAPAction": "urn:getFullQuote"}
			conn = http.client.HTTPConnection("localhost", 8280, timeout=3000)
			conn.request("POST", "/services/vfs_{0}".format(i), sampleSoapMessage.format(i), headers)
			response = conn.getresponse()
			print(response)
			print(" ---- Thread ----- " + self.getName())


for i in range(numberOfconcurrency):
	t = ThreadClass()
	t.start()

