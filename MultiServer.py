from socket import *
import sys
import threading

# Function to handle each client request
def handle_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode('iso-8859-1')
        print(f"[{addr}] Received request:")
        print(message)

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()

        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

    except IOError:
        error_message = "HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>\r\n"
        connectionSocket.send(error_message.encode())

    connectionSocket.close()
    print(f"[{addr}] Connection closed.")

# Main server setup
serverSocket = socket(AF_INET, SOCK_STREAM)
hostname = gethostname()
server_ip = gethostbyname(hostname)
print(f"Server IP: {server_ip}")

serverSocket.bind(('', 6789))
serverSocket.listen(5)  # Can queue up to 5 incoming connections

print("Multithreaded server ready to serve...")

# Accept connections in a loop
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"[{addr}] Connection accepted.")

    # Start a new thread for each client
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()
