import packetAnalyzer
import json
from sites import *
import time
import socket
from sendData import *



def writeJson(d):  #not yet implemented

	size = len(d)
	for key in sorted(d, key = lambda name: d[name].getSize()):
		#print "dividing  100/",size 
		d[key].setRadius((100/size)+10)
		size -=1
		
		#print d[key].getName(), d[key].getSize()
	with open('data.json', 'w') as fp:
		fp.write("[")
		for key in d:
			json.dump(d[key].getJSON(), fp)
			if (key != d.keys()[-1]):
				fp.write(',')
			fp.write('\n')
		fp.write("]")
	fp.close()
	client()

	# s = socket.socket()         # Create a socket object
	# host = '146.95.219.133' # Get local machine name
	# port = 12348                 # Reserve a port for your service.

	# s.connect((host, port))
	# s.send("Hello server!")
	# f = open('data.json','rb')
	# print 'Sending...'
	# l = f.read(1024)
	# while (l):
	#     print 'Sending...'
	#     s.send(l)
	#     l = f.read(1024)
	# f.close()
	# print "Done Sending"
	# # s.send("STOP")
	# print s.recv(1024)
	# s.shutdown(2)
	# s.close    

