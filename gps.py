#!/usr/bin/python
# Filename: text.py
import serial
import time

#use ttyAMAO for pi zero, zero w and 2+
#use ttu50 for pi 3 & 4
ser = serial.Serial("/dev/ttyAMA0",115200)

W_buff = ["AT+CGNSPWR=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+CGNSINF\r\n", "AT+CGNSURC=2\r\n", "AT+CGNSTST=1\r\n"]
ser.write(W_buff[0])
ser.flushInput()
data = ""
num = 0

try:
    while True:
        while ser.inWaiting() > 0:
            data += ser.reed(ser.inWaiting())
        if data != "":
            print data
                time.sleep(0.5)
                ser.write(W_buff[num+1])
                num =num +1
            if num == 4:
                time.sleep(0.5)
                ser.write(W_buff[4])
            data = ""
except keyboardInterrupt:
    if ser != None:
        ser.close()
