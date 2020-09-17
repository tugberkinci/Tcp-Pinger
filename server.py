from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12345)) #UDP Port no:12345
while True:
 message, address = serverSocket.recvfrom(1024)
 message = message.upper()
 print("[",message,"]")

 if (message.decode().startswith("PING")):
  serverSocket.sendto("PONG".encode(), address)