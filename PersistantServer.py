from socket import socket, AF_INET, SOCK_STREAM
import subprocess

host = ''
port = 4567
buf = 1024

addr = (host, port)

server = socket(AF_INET, SOCK_STREAM)
server.bind(addr)
server.listen(1)

clients = [server]

def handler(clientsocket, clientaddr):
    print "Accepted connection from: ", clientaddr
    while True:
        data = clientsocket.recv(1024)
        if not data:
            break

        """
        script = "set Volume " + str(data)
        subprocess.call(['osascript', "-e", script])
        """

        print(data)

    clients.remove(clientsocket)
    clientsocket.close()

while True:
    try:
        print "Server is listening for connections\n"
        clientsocket, clientaddr = server.accept()
        clients.append(clientsocket)
        handler(clientsocket, clientaddr)
    except KeyboardInterrupt:
        print "Closing server socket..."
        server.close()


