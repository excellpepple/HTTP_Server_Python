import sys
from socket import *

def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_host> <server_port> <filename>")
        sys.exit()

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    # Create a TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    try:
        # Connect to the server
        clientSocket.connect((server_host, server_port))

        # Construct and send GET request
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
        clientSocket.send(request.encode())

        # Receive and print the response
        response = b""
        while True:
            chunk = clientSocket.recv(1024)
            if not chunk:
                break
            response += chunk

        print("Server response:\n")
        print(response.decode('iso-8859-1'))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        clientSocket.close()

if __name__ == "__main__":
    main()
