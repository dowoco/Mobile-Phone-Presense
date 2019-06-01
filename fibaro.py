#!/usr/bin/python

import requests, json

#currently has to be the superuser to allow Global Variables to be updated
auth=('user@domain.com', 'PASSWORD')
url = "http://192.168.1.1/api/globalVariables/"
statusfile = "status.txt"

def do_request(path, method="GET", params={}, headers={}):
	if method == "GET":
        	response = requests.get(path, headers=headers, auth=auth)
    	elif method == "POST":
            	headers["Content-Type"] = "application/json"
            	response = requests.post(
                	path,
                	data=json.dumps(params),
                	headers=headers,
                	auth=auth)
        elif method == "PUT":
            	headers["Content-Type"] = "application/json"
            	response = requests.put(
                	path,
                	data=json.dumps(params),
                	headers=headers,
                	auth=auth)
        elif method == "DELETE":
            	response = requests.delete(
                	path,
                	data=json.dumps(params),
                	headers=headers,
                	auth=auth)
        return response

def set_global_value(code, value):
        try:
                data = {"name": code, "value": str(value)}
                r = do_request(url+code, "PUT", data)
                #print(r)
                if r.status_code==200:
                        data = r.json()
                        return data
                else:
                        return None
        except requests.exceptions.RequestException as e:  # This is the correct syntax
                print('FIBARO ERROR! Exception {}'.format(e))
                return None
        except: # catch *all* exceptions
                e = sys.exc_info()[0]
                print("FIBARO Unexpected error:", e)
                return None

def get_global_value(code):
        try:
                r = do_request(url+code, "GET")
                #print(r)
                if r.status_code==200:
                        data = json.loads(r.content)
                        value = data['value']
                        return value
                else:
                        return None
        except requests.exceptions.RequestException as e:  # This is the correct syntax
                print('FIBARO ERROR! Exception {}'.format(e))
                return None
        except: # catch *all* exceptions
                e = sys.exc_info()[0]
                print("FIBARO Unexpected error:", e)
                return None


def getPresense(filename):
        people = {}
        f = open(filename,"r")

        for line in f:
                (name, status) = line.split()
                people[(name)] = status
        f.close()
        return people

family = {}
family = getPresense(statusfile)

#print family

for name, status in family.items():
	set_global_value(name, status)
