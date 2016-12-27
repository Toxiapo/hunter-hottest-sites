import time
from packetAnalyzer import *
import multiprocessing


def main():
    global trigger
    p = multiprocessing.Process(target=startCapture, name="startCapture")

    p.start()
    time.sleep(6000)   #Time to run capture
    p.terminate()
    p.join()

    print "Packet capture terminated"
main()
