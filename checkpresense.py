#!/usr/bin/python

import os,time
phonesfile = "/home/pi/family"
statusfile = "/home/pi/status.txt"
presenseStatus = {}

def networkping(host):
	response = os.system("fping -c1 -b 32 -t1000 " + host + " 2>/dev/null 1>/dev/null")
	return int(response)


def bluetoothping(host):
        response = os.system("l2ping -c1 -s32 -t1 " + host + ">/dev/null 2>&1")
        return int(response)


def getPhones(filename):
	phones = {}
	f = open(filename,"r")

	for line in f:
 		(name, ip, mac) = line.split()
 		phones[(name)] = ip + "," + mac
	f.close()
	return phones

def writeStatus(filename,statusdict):
	f = open(filename,"w")
	for name, status in statusdict.items():
		f.write(name + " " + status + "\n")
	f.close()



phonesList = {}
phonesList = getPhones(phonesfile)

for name, address in phonesList.items():
	addresses = address.split(",")
	ipaddress = addresses[0]
	macddress = addresses[1]
	presenseStatus[name] = "Away"
	for x in range(0, 1):
		#print "IP " + name + " " + str(networkping(ipaddress)) + " " + ipaddress
		if networkping(ipaddress) == 0:
			presenseStatus[name] = "Home"
			#print  name + " IP break"
			break

		#print "MAC " + name + " " + str(bluetoothping(macddress)) + " " + macddress
		if bluetoothping(macddress) == 0:
                        presenseStatus[name] = "Home"
			#print name + " MAC break"
                        break
		time.sleep(3)
#print presenseStatus

writeStatus (statusfile,presenseStatus)
