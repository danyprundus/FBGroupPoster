import serial
import csv
import sys
# Program that reads from the arduino
import serial, io, time
from time import strftime

device = '/dev/cu.usbmodem1421'

ser = serial.Serial(device, 9600, timeout=None)
print("Connected to: " + ser.portstr)
line = ser.readline()
print(line)
while True:
    line = ser.readline()
    dt = strftime("%Y-%m-%d %H:%M:%S")
    print dt, line
print 'Done.'
ser.close()