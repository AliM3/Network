#TCPClient.py

from socket import socket, AF_INET, SOCK_STREAM
serverName = 'localhost'
serverPort = 8888
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Input lowercase sentence: ')
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(2048).decode()
print ('From Server: ', modifiedMessage)
clientSocket.close()