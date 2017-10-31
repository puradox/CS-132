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

def expect(command, expectedCode):
    clientSocket.send(command.encode())
    print(command, end="")
    response = clientSocket.recv(1024).decode()
    print('>', response, end="")
    if response[:3] != str(expectedCode):
        print(str(expectedCode), 'reply not received from server.')

# Send HELO command
expect('HELO Alice\r\n', 250)

# Send MAIL FROM command
expect('MAIL FROM: <sbalana@uci.edu>\r\n', 250)

# Send RCPT TO command
expect('RCPT TO: <sbalana@uci.edu>\r\n', 250)

# Send DATA command
expect('DATA\r\n', 354)

# Send message data (ending with a single period)
expect(message + endSequence, 250)

# Send QUIT command
expect('QUIT\r\n', 221)
