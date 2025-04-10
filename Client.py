from socket import *

# from pyexpat.errors import messages

server_name = "10.100.239.167"
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM) #creates a udp connection
message = input("input lowecase sentence: ") #ask for input

client_socket.sendto(message.encode(), (server_name, server_port)) #sends the info to the server after encoding it
modified_message, server_address = client_socket.recvfrom(2048) #waits to recieve a response

print(modified_message.decode())
client_socket.close()
