#!/usr/bin/python

from socket import *
from sys import argv

msg="Welcome to Hell"

#creer une socket en UDP
s=socket(AF_INET, SOCK_DGRAM)

server=argv[1]
print server, "addresse IP:",gethostbyname[server]


s.sendto(msg,(server,7777))
(data, addr) = s.recvfrom(512)

if data==msg:
	print "ok"
else:
	print "erreur"
