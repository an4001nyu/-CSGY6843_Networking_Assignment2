# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:

        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print(f'Connection from {addr} has been established')

        try:
            message = connectionSocket.recv(1024).decode()  # receive message from client, 1024 is buffer size
            filename = message.split()[1]

            f = open(filename[1:])  # open file

            outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
            connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")

            print(f'{outputdata}')

            for i in f:
                connectionSocket.send(str.encode(i))
            print('sent successfully!')
            connectionSocket.close()

        except Exception as e:
            connectionSocket.send(b"HTTP/1.1 404 File Not Found\r\n\r\n")
            connectionSocket.close()
            # sys.exit()

    serverSocket.close()
    # sys.exit()


if __name__ == "__main__":
    webServer()
