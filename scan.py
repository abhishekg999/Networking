import socket
import sys

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

if isOpen(sys.argv[1], int(sys.argv[2])):
    print("%s : %s is open" % (sys.argv[1], sys.argv[2]))
else:
    print("%s : %s is closed" % (sys.argv[1], sys.argv[2]))



