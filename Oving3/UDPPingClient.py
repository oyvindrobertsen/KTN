import sys
import socket
from datetime import datetime

address = ('', 12000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)


def ping_function(count):
    for i in xrange(count):
        msg = 'Ping ' + str(i) + ' ' + str(datetime.now())
        try:
            client_socket.sendto(msg, address)
            response, addr = client_socket.recvfrom(1024)
            rtt = datetime.now() - datetime.strptime(' '.join(response.split(' ')[2:]), '%Y-%m-%d %H:%M:%S.%f')
            print response + ', RTT = ' + str(rtt.total_seconds()) + 's'
        except Exception, e:
            print 'Ping ' + str(i) + ' ' + str(e)


if len(sys.argv) > 1:
    ping_function(int(sys.argv[1]))  # First argument is always filename, second is
                                  # optional number of packets to send.
else:
    ping_function(10)             # If called with no arguments, send 10 packets
