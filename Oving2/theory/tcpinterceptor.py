from socket import *

PORT = 3456
HOST = ''

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind((HOST, PORT))

serversocket.listen(1)
print 'Server running on http://localhost:', PORT

while True:
    connectionSocket, addr = serversocket.accept()
    print connectionSocket.recv(3000)
