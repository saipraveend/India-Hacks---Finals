import socket, traceback
import os
import os.path
import time
import math

#Common To Sensor_Stream and Hand_Orientation_Stream
host = ''

#Port List
ss_port = 5550
ho_port = 5500


#Sensor Binding to Port
sensor_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hand_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sensor_s.setblocking(False)
hand_s.setblocking(False)

sensor_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sensor_s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

hand_s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
hand_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sensor_s.bind((host,ss_port))
hand_s.bind((host,ho_port))

while True:
    try:
            global gyroX
            message_s, address = sensor_s.recvfrom(100)
            print message_s
            message = message_s.split(",");
            accX = float(message[0])
            accY = float(message[1])
            accZ = float(message[2])
            gyroX = float(message[3])
            gyroY = float(message[4])
            gyroZ = float(message[5][:-1])
            
            #print "gyroX = " + gyroX
            sensor_s.flush()
    except:
            pass


	    
