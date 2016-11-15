import packetAnalyzer
import json
from sites import *
import time
import socket
from sendData import *



def writeJson(d):  #not yet implemented

	# size = len(d)
	# for key in sorted(d, key = lambda name: d[name].getSize()):
	# 	d[key].setRT(150*(math.log(1+100,2)/math.log(1+1000,2)) )
	# 	#print "dividing  100/",size 


	# 	d[key].setRT((100/size)+25)
	# 	size -=1

	# size = len(d)
	# for key in sorted(d, key = lambda name: d[name].getCount()):
	# 	if(size == len(d)):
	# 		for key in d:
	# 			d[key].setMaxIP((100/size)+25)
	# 	size -=1

	# size = len(d)
	# for key in sorted(d, key = lambda name: d[name].getIPlength()):
	# 	#print "dividing  100/",size 
	# 	d[key].setRU((100/size)+25)
	# 	size -=1

		#print d[key].getName(), d[key].getSize()
	with open('data.json', 'w') as fp:

		fp.write("[")
		for key in d:
			json.dump(d[key].getJSON(), fp)
			if (key != d.keys()[-1]):
				fp.write(',')
			fp.write('\n')
		fp.write("]")
	print "wrote json"
	fp.close()
	client()   #calls the client script to send the file

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

