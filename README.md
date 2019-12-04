# Smart_racks_IOT


IOT smart racks final project

The goal of the project is to design a smart rack. Each drawers in the smart rack are designed to store various items and would require constant monitoring of the environment of the drawer. 

-For this purpose each drawer is equipped with a sensor node/client node, i.e., Zolertia Z1 embeding temperature and humidity sensor in it. 
-Client nodes periodically sends captured data values using udp-client.c to the central server Zolertia connected to Rpi on each rack which runs the udp-server.c.
-RPi logs this received data into an online IoT server 'UbiDots' using smart_rack_api.py. Also it maintain the temperature of each drawers in order to act at times when the temperature falls below a certain threshold.
Interface-1: Establish 6LoWPAN communication

INTERFACE- 1: Establish 6LoWPAN communication
Client Zolertia:
•Assign Specific node-ID to each sensor Nodes.
•Modify send_packets() of client program to read temperature data for every 15 seconds.
•IPV6 UDP_CLIENT script sends and receives message.
Server Zolertia:
•IPV6 UDP_SERVER script sends and receives message.
•Analyse data and send back control signal- ‘ON/OFF’.
Temperature Control:
•tcpip_handler() in client listens to control signal from server and uses led.h library in UDP_CLIENT program to switch ON/OFF LEDs in zolertia.

INTERFACE- 2: Communicating to Ubidots and Data Analysis
Login to Ubidots server and obtain unique API-key/Token
Raspberry Pi: Python script is written
•USB Serial programming to read data from server Zoleria
•Segregates data into separate .csv files based on nodeid
•Connects to Ubidots every 15 seconds using Request python library, Restful API and unique token received.

