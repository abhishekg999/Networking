import socket
import sys
import threading
import time
import os

from queue import Queue

print_lock = threading.Lock()
socket.setdefaulttimeout(2)

target_host = sys.argv[1]

logfile = str("log" + str(int(round(time.time() * 1000))) + ".txt")

def portscan(portadd):
	target_port = portadd
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	try:
		
		con = client.connect((test_host, target_port))
		with print_lock:
			print ('%s : %s open' % target_host, target_port)
			c = ("echo " + ('%s : %s open' % target_host, target_port) + " >> " + logfile)
			os.system(c)
		
		con.close()
		
	except:
		with print_lock:
			print("not: " + target_host + " : " + str(target_port))
		pass


def threader():
	while True:
		worker = q.get()
		portscan(worker)	
		q.task_done()
		
q = Queue()

for x in range(100):
	t = threading.Thread(target=threader)
	t.setDaemon(True)
	t.start()
	
start = time.time()

for worker in range(1, int(sys.argv[2])):
	q.put(worker)


q.join()
print(time.time() - start)



