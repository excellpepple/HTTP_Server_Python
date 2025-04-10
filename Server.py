# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
hostname = gethostname()
server_ip = gethostbyname(hostname)
print(f"Server IP: {server_ip}")

serverSocket.bind(('', 6789))  # Bind to all interfaces on port 6789
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode('iso-8859-1')  # Safer decode for HTTP
        print("Received message:")
        print(message)

        filename = message.split()[1]
        f = open(filename[1:])  # Strip leading slash
        outputdata = f.read()
        f.close()

        # Send HTTP response header
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())

        # Send the content of the requested file
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

    except IOError:
        # Send 404 response if file not found
        error_message = "HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>\r\n"
        connectionSocket.send(error_message.encode())

    connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
