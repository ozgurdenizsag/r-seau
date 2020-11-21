#!/usr/bin/python
##
# proxy TCP
##
from socket import *
from sys import argv
from select import select

if len(argv) <> 4:
  print "usage: %s port rhost rport"
  exit(1)
port=int(argv[1])
rhost=gethostbyname(argv[2])
rport=int(argv[3])
# create server socket
s=socket(AF_INET, SOCK_STREAM)
s.bind(('0.0.0.0', port))
s.listen(1)
print ">>> Listening on port " + str(port)
(c,addr)=s.accept()
print ">>> Connection from " + str(addr)
r=socket(AF_INET, SOCK_STREAM)
r.connect((rhost, rport))
go=True
while go:
  lin, out, lex = select([c,r],[],[])
  for x in lin:
    if x==c:
      y=r
      hd="> "
    else:
      y=c
      hd="< "
    data=x.recv(4096)
    if data:
      print hd + data,
      if go:
        y.send(data)
    else:
      print hd + "[closing socket]"
      y.close()
      go=False

