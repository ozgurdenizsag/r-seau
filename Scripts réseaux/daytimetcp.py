#!/usr/bin/python

from socket import *
from datetime import datetime

s= socket(AF_INET, SOCK_STREAM)

s.bind(('0.0.0.0',13))

s.listen(3)

print "listening on port 13"

while True:
	(c,addr) = s.accept() #attend que le client se connecte

	print "request from " + str(addr)

	c.send(datetime.now().strftime('%c\n'))
	c.close()
