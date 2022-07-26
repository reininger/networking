# TCP server
from socket import *

serverPort = 12000
messageBufferLen = 2048

with socket(AF_INET, SOCK_STREAM) as serverSocket:
	serverSocket.bind(('', serverPort))
	serverSocket.listen(1)
	print('The server is ready to receive')
	while True:
		connectionSocket, addr = serverSocket.accept()
		with connectionSocket:
			message = connectionSocket.recv(messageBufferLen).decode()
			capitalizedMessage = message.upper()
			connectionSocket.send(capitalizedMessage.encode())

