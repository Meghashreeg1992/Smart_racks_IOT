# Smart_racks_IOT


IOT smart racks final project

The goal of the project is to design a smart rack. Each drawers in the smart rack are
designed to store various items and would require constant monitoring of the environment
of the drawer. 

For this purpose each drawer is equipped with different sensors, i.e.,
humidity and temperature sensors, and a sensor node, i.e., Zolertia Z1. 
The nodes should periodically update the captured values using udp-client.c to the central
server on each rack which runs the udp-server.c. This node in turn will store the values 
in an online IoT service through raspberry pi through the smart_rack_api.py. Also
the central server also should maintain the temperature of each drawers in order to act at
times when the temperature falls below a certain threshold.
