from socket import *

server_name = gethostname()
sever_port = 12000
server_ip = gethostbyname(server_name)
print(f"Server IP: {server_ip}")

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, sever_port))

sentence = input("Enter a sentence: ")
client_socket.send(sentence.encode())

modified_sentence = client_socket.recv(1024)

print(modified_sentence.decode())
client_socket.close()