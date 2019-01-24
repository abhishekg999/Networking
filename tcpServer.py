import sys
import socket

IP = ''
PORT = 4567

BUFFER_SIZE = 50

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP, PORT))

server.listen(1)

conn, addr = server.accept()

print "Connected at ",  addr

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print data

    conn.send(data)

conn.close()