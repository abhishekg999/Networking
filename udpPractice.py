import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.sendto("ABCABCABC", (target_host, target_port))

data, addr = client.recvfrom(4096)

print(data)
