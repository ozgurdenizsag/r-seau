#!/usr/bin/python
##
# Simple SMTP client 
##
from socket import *
from sys import argv

if len(argv)<>2:
  print "usage: %s mail" % argv[0]
  exit(1)

# create a TCP socket instance
s=socket()
# connecting to server on port 25
s.connect(("smtp.iiia.net",25))

print s.recv(512)
s.send('HELLO l3ing\n')


print s.recv(512)

s.send('MAIL FROM: <noreply@domain.name>\n')
print s.recv(512)

s.send('RCPT TO: <guest@iiia.net>\n')
print s.recv(512)

s.send('DATA\n')
print s.recv(512)


msg="Subject: bienvenu\n\
Bienvenu dans ce cours de TP\n\
.\n"

s.send(msg)
print s.recv(512)

s.send('QUIT')
print s.recv(512)

exit(0)
#s.close()




# transform server name into IP address
#sname=argv[1]
#server=gethostbyname(sname)
#print "%s address is %s" % (sname, server)

# send HTTP GET method
#s.send("""GET / HTTP/1.0
#Host: %s
#Accept: */*

#""" % (sname,))
#r=''
#while True:
#  data=s.recv(4096)
#  if data:
 #   r=r+data
 # else:
 #   print r
#    exit(0) 
