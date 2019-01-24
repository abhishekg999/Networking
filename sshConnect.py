
try:
	import sys, paramiko
except ImportError:
	print(Exception)
	print("\n Did you forget python3?")
	sys.exit(1)

import socket
import sys
import threading
import time
import os
import argparse

from queue import Queue

print_lock = threading.Lock()
socket.setdefaulttimeout(2)

iplist = []

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('1.2.3.4', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def trimIP(my):
	tempIP = ""
	count = 0
	
	for char in my:
		if char != '.' and count != 3:
			tempIP += char
		
		elif char == '.' and count != 3:
			count += 1		
			tempIP += char
			
		elif count >= 3:
			return tempIP

def getHostAddr(my):
	return trimIP(my)


try:
	target_host = getHostAddr(sys.argv[2])

except IndexError:
	target_host = getHostAddr(getIP())




try:
	target_port = int(sys.argv[1])
except IndexError:
	print ("Target port not set...")
	print ("Defaulting to port 22")
	target_port = 22


logfile = str("log" + str(int(round(time.time() * 1000))) + ".txt")

def ipscan(ipadd):
	test_host = target_host + str(ipadd)	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	try:
		
		con = client.connect((test_host, target_port))
		with print_lock:
			print ('ip %s open' % test_host)
			c = ("echo " + ('ip %s open' % test_host) + " >> " + logfile)
			iplist.append(test_host)
			os.system(c)
		
		con.close()
		
	except:
		with print_lock:
			print("not: " + test_host + " : " + str(target_port))
		pass


def threader():
	while True:
		worker = q.get()
		ipscan(worker)	
		q.task_done()
		
q = Queue()

for x in range(100):
	t = threading.Thread(target=threader)
	t.setDaemon(True)
	t.start()
	
start = time.time()

for worker in range(1,255):
	q.put(worker)


q.join()
print(time.time() - start)

#---------------------------------------------------------------------------------#

def sshscan(index):
	
	try:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		
		client.connect(iplist[index], port, username, password)

		working.append(iplist[index])
		c = ("echo " + (iplist[index]) + " >> " + logfile)
		with print_lock:
			print(iplist[index] + " working")

		os.system(c)
		client.close()

	except:
		pass

def sshthreader():
	while True:
		worker = e.get()
		sshscan(worker)
		e.task_done()




working = []


password = sys.argv[3]
username = "student"
port = 22


ans = input("Continue: ")
print(iplist)

if ans.lower == "y" or "yes":
	e = Queue()

	for x in range(100):
		t = threading.Thread(target=sshthreader)
		t.setDaemon(True)
		t.start()

	for worker in range(len(iplist)):
		e.put(worker)

	e.join()


	

print(working)