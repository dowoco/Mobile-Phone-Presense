# Mobile-Phone-Presense
Check groups of phones to see who is home and store in log file

This script is written in Python and deployed on a Raspberry PI 3 with Bluetooth and WiFi. The is script also relies on other software like: Fping and L2ping


There are two files:

checkpresense.py - Holds the Python code and must be run as Root for the l2ping command to detect Bluetooth devices

family - Can hold a list of devices to check. The format of this file is as follows:
    
    Key(this should be a unique name to identify this device)
    IP Address of the WiFi adaptor
    MAC address of the Bluetooth adaptor
    
    e.g. Key1 192.168.1.1 D4:09:3E:2S:ME:58
    
