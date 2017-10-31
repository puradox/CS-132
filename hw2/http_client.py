import sys
import socket

def get(hostname, port, filename):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((hostname, port))

    request = (
        'GET ' + filename + ' HTTP/1.1\r\n'
        'Host: ' + hostname + '\r\n'
    )

    clientSocket.send(bytes(request, 'utf-8'))

    result = ""
    buffer = clientSocket.recv(1024)

    while buffer:
        result += str(buffer, 'utf-8')
        buffer = clientSocket.recv(1024)

    clientSocket.close()

    return result

print(get(sys.argv[1], int(sys.argv[2]), sys.argv[3]))