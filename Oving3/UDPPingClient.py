import sys
from socket import *
from datetime import datetime

address = ('', 12000)
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

if len(sys.argv) > 1:
    for i in xrange(int(sys.argv[1])):
        msg = 'Ping     ' + str(i) + '       ' + str(datetime.now())
        try:
            client_socket.sendto(msg, address)
            print client_socket.recvfrom(1024)
        except Exception, e:
            print e
