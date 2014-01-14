#import socket module 
from socket import *

serverPort = 8081
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print 'Server running on port ' + str(serverPort)
while True:    
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        print message.split()[0] + ' ' + filename
        if filename == '/':
            f = open('index.html')
        else:
            f = open(filename[1:])
        outputdata = f.readlines()

        response_body_raw = ''.join(outputdata)

        response_proto = 'HTTP/1.1'
        response_status = '200'
        response_status_text = 'OK'

        response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(response_body_raw),
            'Connection': 'close',
        }

        response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in response_headers.iteritems())

        connectionSocket.send('%s %s %s' % (response_proto, response_status, response_status_text))
        connectionSocket.send(response_headers_raw)
        connectionSocket.send('\n')
        connectionSocket.send(response_body_raw)

        connectionSocket.close()
    except IOError:
        response_proto = 'HTTP/1.1'
        response_status = '404'
        response_status_text = 'File not found'

        connectionSocket.send('%s %s %s' % (response_proto, response_status, response_status_text))
        connectionSocket.send('Connection: close')
        connectionSocket.send('\n')
        connectionSocket.send('<h1>404 File not found</h1>')


        connectionSocket.close()
    except IndexError:
        response_proto = 'HTTP/1.1'
        response_status = '500'
        response_status_text = 'Internal Server Error'

        connectionSocket.send('%s %s %s' % (response_proto, response_status, response_status_text))
        connectionSocket.send('Connection: close')
        connectionSocket.send('\n')
        connectionSocket.send('<h1>500 Internal Server Error</h1>')

        connectionSocket.close()

serverSocket.close()
