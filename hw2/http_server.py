import os
import socket
import threading


def handle(clientSocket):
    try:
        data = clientSocket.recv(1024)
        message = str(data, 'utf-8')
        print(message)
        filename = message.split()[1]
        fileSize = os.path.getsize(filename[1:])

        # Send HTTP response status line
        response = (
            'HTTP/1.1 200 OK\r\n'
            'Content-Size: ' + str(fileSize) + '\r\n'
            '\r\n'
        )
        clientSocket.send(bytes(response, 'utf-8'))

        # Send requested file
        with open(filename[1:], "rb") as infile:
            buffer = infile.read(1024)
            while buffer:
                clientSocket.send(buffer)
                buffer = infile.read(1024)

        clientSocket.close()
    except IOError:
        # File not found
        response = (
            'HTTP/1.1 404 Not Found\r\n'
            '\r\n'
        )
        clientSocket.send(bytes(response, 'utf-8'))
        clientSocket.close()


def listen():
    # Aquire a server socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((socket.gethostname(), 80))

    # Listen for connections, refuse any more connections after 1.
    serverSocket.listen(5)
    print("Listening on port 80\n")

    while True:
        # Accept connections from outside
        (clientSocket, address) = serverSocket.accept()
        print("Accepted client from " + str(address[0]) + ":" + str(address[1]))
        connection = threading.Thread(target=handle, args=(clientSocket,))
        threads.append(connection)
        connection.start()

    serverSocket.close()

threads = []
mainThread = threading.Thread(target=listen)
threads.append(mainThread)
mainThread.start()
