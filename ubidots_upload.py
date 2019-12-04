import time
import requests
import math
import random
import csv 
import sys

TOKEN = "BBFF-2DcrBoQtrSLVt2bVj3lpm18PYNAHae"  # Put your TOKEN here
#TOKEN = "A1E-lXiWols4GB3GqtHs8CAGKGXKDuDPnD"
DEVICE_LABEL = "Smart"  # Put your device label here 
VARIABLE_LABEL_1 = "temp_131"  # Put your first variable label here
VARIABLE_LABEL_2 = "temp_132"  # Put your second variable label here
#VARIABLE_LABEL_3 = "position"  # Put your second variable label here


def build_payload(variable_1, value):
    # Creates two random values for sending data
    #value_1 = temp
    #value_2 = temp2
    payload = {variable_1: value}
    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    global temp, temp2
    #temp=20
    #temp2=20
    r = open('sensor.csv', 'r')
    reader = csv.reader(r)
    for row in reader:
    	if (row[2]== "131"):
	    print("Z1")
	    temp = (row[1])
	    print(temp)
	    payload = build_payload(VARIABLE_LABEL_1, temp)
	else:
	    print("Z2")
	    temp = (row[1])
	    print(temp)
	    payload = build_payload(VARIABLE_LABEL_2, temp)
    #print(temp,temp2)
   
   # payload = build_payload(VARIABLE_LABEL_1)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
    sys.exit(0)


if __name__ == '__main__':
    while (True):
        main()
        
