from socket import *
msg = "From: oyvinrob@stud.ntnu.no\r\nTo: oyvinrob@stud.ntnu.no\r\nSubject: testemail\r\nI love computer networks!\r\n"
endmsg = ".\r\n"
#Choose a mail server
mailserver = ('smtp.stud.ntnu.no', 25)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(mailserver)

recv = client_socket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server'

# Send HELO command and print server response
helo_command = 'EHLO oyvind\r\n'
client_socket.send(helo_command)
recv1 = client_socket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server'

# Send MAIL FROM command and print server response
mail_from_command = 'MAIL FROM: oyvinrob@stud.ntnu.no\r\n'
client_socket.send(mail_from_command)
recv2 = client_socket.recv(1024)
print recv2
if recv2[:3] != '250':
    print '250 reply not received from server'

rcpt_to_command = 'RCPT TO: oyvinrob@stud.ntnu.no\r\n'
client_socket.send(rcpt_to_command)
recv3 = client_socket.recv(1024)
print recv3
if recv3[:3] != '250':
    print '250 reply not received from server'

# Send DATA command and print server response
data_command = 'DATA\r\n'
client_socket.send(data_command)
recv4 = client_socket.recv(1024)
print recv4
if recv4[:3] != '354':
    print '354 reply not received from server'



# Send message data and terminator
client_socket.send(msg)
client_socket.send(endmsg)
recv5 = client_socket.recv(1024)
print recv5
if recv5[:3] != '250':
    print '250 reply not received from server'

quit_command = 'QUIT\r\n'
client_socket.send(quit_command)
recv6 = client_socket.recv(1024)
print recv6
if recv6[:3] != '221':
    print '221 reply not received from server'
