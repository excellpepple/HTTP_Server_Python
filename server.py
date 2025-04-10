from socket import *

server_ip = gethostbyname(gethostname())
print(f"Server IP: {server_ip}")
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print("the server is ready to receive")

while True:
    connection_socket, client_address = server_socket.accept()
    sentence = connection_socket.recv(1024).decode()
    modified = sentence.upper()
    connection_socket.send(modified.encode())
    connection_socket.close()

