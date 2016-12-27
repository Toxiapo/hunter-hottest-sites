import pyshark
import datetime
import websocket

# ws = websocket.create_connection("ws://104.131.81.160:8080")

ranges = []
lastMinute = {}
currentRange = datetime.datetime.now()

def examinePacket(packet):
    global currentRange
    global lastMinute
    try:
        domain = packet.dns.qry_name
        print domain
        # if in range
        if (datetime.datetime.now() - currentRange).seconds > 300:
            ranges.append(lastMinute)
            print ranges
            currentRange += datetime.timedelta(0,300)
            lastMinute = {}

        if not domain in lastMinute:
            lastMinute[domain] = 0
        lastMinute[domain] += 1

    except AttributeError as e:
        #ignore packets that aren't TCP/UDP or IPv4
        pass

def startCapture():
    capture = pyshark.LiveCapture(interface='en0', display_filter='dns')    #creates a new pyshark object with a specific interface and desired parameters
    capture.apply_on_packets(examinePacket)                                 #sends every packet to the examinePAcket function above to examine them
