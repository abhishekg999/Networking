#!/usr/bin/env python
import socket
import sys

target_host = sys.argv[1]
target_port = int(sys.argv[2])

BufferSize = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    temp = int(target_host[0])
    print (temp)
except:
    target_host = socket.gethostbyname(target_host)

print ("IP Found : " + target_host)

client.connect((target_host, target_port))

print ("Client at %s : %d connected..." % (target_host, target_port))

while True:

    data = raw_input("TCP Send: ")

    client.send(data)

    print("'%s' sent to %s : %d" % (data, target_host, target_port))
    try:
        client.settimeout(5.0)
        print client.recv(1024)
    except socket.timeout:
        print("%s timed out in 5.0 seconds" % target_host)
