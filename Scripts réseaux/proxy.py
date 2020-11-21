#!/usr/bin/python
##
# TCP chat server
# port 1664
##
from socket import *
from select import select
from sys import argv

if len(argv)<>4:
  print "Nombre de paramettre manquant pour : ", argv[0]
  exit(1)


