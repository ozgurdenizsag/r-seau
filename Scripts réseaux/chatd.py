#!/usr/bin/python
##
# TCP chat server
# port 1664
##
from socket import *
from select import select

# create an TCP socket instance
s=socket(AF_INET, SOCK_STREAM)
# associate the socket to local port 1664
s.bind(('0.0.0.0', 1664))
# create a waiting queue
s.listen(3)
print "Listening on port 1664"
# list of currently open sockets
socks=[s]
while True:
  # wait for an incoming message
  lin, lout, lex=select(socks, [], []) 
  print "select got %d read events" % (len(lin))
  for t in lin:
    if t==s: # this is an incoming connection
      (c, addr)=s.accept()
      msg="Hello %s\n" % (addr[0],)
      print msg
      socks.append(c)
      c.send(msg) 
    else: # someone is speaking
      who=t.getpeername()[0]
      data=t.recv(1024)
      if data:
        msg="%s: %s\n" % (who, data.strip())
      else: # connection closed
        socks.remove(t)
        msg="Goodbye %s!\n" % (who,)
      print msg
      for c in socks[1:]:
        c.send(msg)
