import socket

# Contants
mailserver = "localhost" # Make sure you're on an EECS server
endSequence = '\r\n.\r\n'
message = '\r\n I love computer networks!'

# Connect to mail server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, 25))
response = clientSocket.recv(1024).decode()
print(response)

if response[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
response = clientSocket.recv(1024).decode()
print(response)

if response[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command
# Send RCPT TO command
# Send DATA command
# Send message data
# Message ends with a single period
# Send QUIT command
