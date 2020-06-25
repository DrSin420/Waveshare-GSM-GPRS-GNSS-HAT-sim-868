import serial
import time

#use ttyAMAO for pi zero, zero w and 2+
#use ttu50 for pi 3 & 4
ser = serial.Serial("/dev/ttyAMA0",115200)
# change contact number bellow and msg
W_buff = ["AT\r\n", "AT+CMGF=1\r\n", "AT+CSCA=\"+8613800755500\"\r\n", "AT+CMGS=\"insert number here\"\r\n", "insert msg here"]
ser.write(W_buff[0])
ser.flushInput()
