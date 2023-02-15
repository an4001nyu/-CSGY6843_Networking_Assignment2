# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind((socket.gethostname(), 13331))
    serverSocket.listen(1) #queue of 1 to handle 1 request at a time

    while True:
        # Establish the connection

        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #accepts connection
        print(f'Connection from {addr} has been established')

        try:
            message = connectionSocket.recv(1024) #receives message from client 1024 is buffer
            print(message)
            filename = message.split()[1] #read filename, set to 1 to not read /

            # opens the client requested file.
            # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:]) #open file
            outputdata=f.read() #read file and store in buffer
            # Fill in start -This variable can store your headers you want to send for any valid or invalid request.
            # Content-Type above is an example on how to send a header as bytes
            # Fill in end

            # Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            # Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
            # Fill in start

            connectionSocket.send('HTTP/1.x 200 OK\r\n\r\n')
            connectionSocket.send("Content-Type: text/html\r\n\r\n")


            # Fill in end

            # Send the content of the requested file to the client
            for i in len(outputdata.end):
                connectionSocket.send(outputdata[i])

            # Fill in start - send your html file contents #Fill in end
                connectionSocket.close()  # closing the connection socket
            print('File Received')

        except Exception as e:
    # Send response message for invalid request due to the file not being found (404)
    # Fill in start
            connectionSocket.send("HTTP/1.x 404 File Not Found\r\n\r\n")
    # Fill in end

    # Close client socket
    # Fill in start
        connectionSocket.close()
    # Fill in end

    # Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data