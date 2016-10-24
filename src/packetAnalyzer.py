
from sites import *
import math
import pyshark
import socket
from jsonExport import *
import time
from datetime import datetime, timedelta

global Max
Max = 0

trigger = True
global endTime
#endTime = int(time.time()) + 1400

d = {}

def examinePacket(pkt):
    global trigger
    global Max
    try:
        destIP = str(pkt.ip.dst)    #strips the destination of the packet (in IP format)
        srcIP = str(pkt.ip.src)     #strips the source of the packet (IP of device)
        traffic = int(pkt.length)   #strips the length of the packet

        if (destIP[0:3] == "146"):  #Filters anything with a 146 address on the first octect (These are hunter's network addresses)
                return

        try:
            destIP = socket.gethostbyaddr(destIP)[0]    #Converts IP to hostname (if it exists)
            destIP = destIP.split('.',destIP.count('.')-1)[-1]

            if(destIP == "akamaitechnologies.com" or destIP == "1e100.net" or destIP == "broadcasthost" or destIP = "mcast.net" or destIP == "hosted-by-100tb.com"):
            	return

            if (destIP == "fbcdn.net"):
            	destIP = "facebook.com"
            if not destIP in d:                         #Creates a new instance of the class, adds it to a dictionary (d), and the hostname is the key
                d[destIP] = SiteData(destIP)
                d[destIP].setMax(Max)

            d[destIP].addIP(srcIP)
            d[destIP].incrementCount()
            d[destIP].incrementTraffic(traffic)
            d[destIP].setMax(Max)

            if(Max < d[destIP].getSize()):
            	Max = d[destIP].getSize()
            	for key in d:
            		d[key].setMax(Max)
            	
            

        except socket.herror as e:
            pass

    except AttributeError as e:
        pass


    #print Max

    # for key in d:
    #     print "traffic size is ", d[key].getSize()
    #     print "Max size is ", d[key].getMax()
        # print "total sites seen: ", len(d)
        # print "-------------------------------------------------------"


    if(int(time.time()) % 11 == 0 and trigger == True):
        print "Writting to json"
        writeJson(d)
        trigger = False
        
    if(int(time.time()) % 12 == 0):
        trigger = True


def startCapture():
    capture = pyshark.LiveCapture(interface='en0', only_summaries=False)    #creates a new pyshark object with a specific interface and desired parameters 
    capture.apply_on_packets(examinePacket)                                 #sends every packet to the examinePAcket function above to examine them
