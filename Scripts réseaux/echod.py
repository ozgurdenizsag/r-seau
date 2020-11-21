#!/usr/bin/python
##
# UDP echo server
# port 7777
##
from socket import *

# create an UDP socket instance
s=socket(AF_INET, SOCK_DGRAM)
# associate the socket to local port 7777
s.bind(('0.0.0.0', 7777))
print "Listening on port 7777"
while True:
  # wait for an incoming message
  (data,addr)=s.recvfrom(512)
  print "%s: %d %s" % (addr, len(data), repr(data))
  # send it back!
  s.sendto(data,addr)
