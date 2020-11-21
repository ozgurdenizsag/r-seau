#!/usr/bin/python
##
# Simple FTP client 
##
from socket import *
from sys import argv

if len(argv)<>2:
  print "usage: %s mail" % argv[0]
  exit(1)

# create a TCP socket instance
s=socket()
server = gethostbyname(argv[1])
# connecting to server on port 21
s.connect((server,21))

print s.recv(4096)
username=raw_input("Name (%s): "%argv[1])
s.send("USER "+username+"\r\n")

print s.recv(4096)
userpass=raw_input("Password: ")
s.send("PASS" +userpass+ "\r\n")

#passage en binary
print s.recv(4096)
s.send("TYPE I\r\n")

command = ""
while (command != "exit"):
	command = raw_input("ftp> ")

	if (command=="exit"):
		s.send('QUIT\r\n')
		print s.recv(4096)

	elif (command[0:2]=="cd"):
		command[3:]
		s.send("CWD "+command[3:]+"\r\n")
		print s.recv(4096)
		
	elif (command=="dir"):
		#passer en mode passiv et recuperer le numero de port
		s.send("PASV\r\n")
		msg =  s.recv(4096)
		print msg

		res = msg[msg.find("(")+1/msg.find(")")].split(",")
		portserver = int(res[4])*256+int(res[5])
		print portserver

		#creer une nouvelle socket s2 vers le server
		s2 = socket()
		s2.connect((server,portserver))		
		# envoyer la commande correspondant a dir au server
		s.send("LIST\r\n")
		print s.recv(4096)
		result = ""
		while True:
			data = s2.recv(8)
			if data:
				result	+= data
			else:
				break

		#fermer la socket s2
		s2.close()
		print result
		print s.recv(4096)

	elif (command[0:3]=="get"):
		#passer ne mode passiv et recuperer le numero de port
		s.send("PASV\r\n")
		msg =  s.recv(4096)
		print msg

		res = msg[msg.find("(")+1/msg.find(")")].split(",")
		portserver = int(res[4])*256+int(res[5])
		print portserver

		#creer une nouvelle socket s2 vers le server
		s2 = socket()
		s2.connect((server,portserver))		
		# envoyer la commande correspondant a get au server
		s.send("RETR"+command[4:]+"\r\n")
		print s.recv(4096)
		#recuperer le resultat dans s2
		result = ""
		while True:
			data = s2.recv(8)
			if data:
				result	+= data
			else:
				break

		#fermer la socket s2
		s2.close()
		
		f = open(command[4:], 'wb') #Writing Binary mode
		f.write(result) 
		f.close()
		print s.recv(4096)

	else:
		pass

print s.recv(512)
s.send('passive\n')

print s.recv(512)
s.send('cd /home/guest\n')

print s.recv(512)
s.send("dir")

print s.recv(512)
s.send('get cake\n')

s.send('EXIT')
print s.recv(512)

exit(0)
