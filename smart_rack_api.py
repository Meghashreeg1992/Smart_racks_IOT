import os
import csv
import sys
import time
import serial
import ubi_test

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=20)
a = [[]]
i = 0

#open("sensor.csv","w").close()

def write_file(str):
    print ("writing")
    #f=open("sensor.csv",'w+')	#Open file to log the data
    #f.write("packet_num,temp_val,node_id\n")
    str.rstrip()
    if str:
	a = str.split(",")
    	print (a[2]+a[1])
	if (len(a) <= 3):
		f=open("sensor.csv",'w+')   #Open file to log the data
    		#s=str(a[0])+","+str(a[1])+","+str(a[2])+"\n"
    		f.write(str)
    		f.close()
		print ("successful")

def read_file():
    global temp
    print ("reading")
    r=open('gps_data.csv','r')  
    reader = csv.reader(r)
    for row in reader:
        temp=(row[1])
        zol=(row[2])
	print(temp)
    return temp

def condition(temp,zol):
    if (temp < "25" and zol=="131"):
        print(temp,zol)
        print("incraese temp in Z1 and 00")
    elif (temp > "25" and zol=="131"):
        print(temp,zol)
	print("no action and 01")
    elif (temp <"25" and zol=="132"):
	print(temp,zol)
        print("incraese temp in Z2 and 11")
    else:
	print(temp,zol)
        print("no action in Z2 and 10")

    print("done")

while True:
#    i= i + 1
    rcv = port.readline()
    write_file(rcv)
    #t,z=read_file()
    #print(t)
    #t=a[1]
    #z=a[2]
    #condition(a[1],a[2])
    #time.sleep(3)
    os.system('ubidots_upload.py')
    #sys.exit(0)
   
