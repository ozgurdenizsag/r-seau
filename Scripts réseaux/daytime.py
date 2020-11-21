#!/usr/bin/python

from socket import *
from datetime import datetime


# create an UDP socket instance
s=socket(AF_INET, SOCK_DGRAM)
# associate the socket to local port 13
s.bind(('0.0.0.0', 13))
print "Listening on port 13"
while True:
  # wait for an incoming message
  (data,addr)=s.recvfrom(512)
  print "%s: %d %s" % (addr, len(data), repr(data))
  # send the date!
  today = datetime.now().strftime('%c\n')
  s.sendto(today,addr)
