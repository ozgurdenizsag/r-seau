#!/usr/bin/python
##
# Simple HTTP client 
##
from socket import *
from sys import argv

if len(argv)<>2:
  print "usage: %s server" % argv[0]
  exit(1)

# transform server name into IP address
sname=argv[1]
server=gethostbyname(sname)
print "%s address is %s" % (sname, server)
# create a TCP socket instance
s=socket()
# connecting to server on port 80
s.connect((server,80))
# send HTTP GET method
s.send("""GET / HTTP/1.0
Host: %s
Accept: */*

""" % (sname,))
r=''
while True:
  data=s.recv(4096)
  if data:
    r=r+data
  else:
    print r
    exit(0) 
