'''
Created on 2. feb. 2015

@author: GGreibesland
'''
from socket import *

serverPort = 12000 # Server port to bind to
serverHostIP = 'localhost' # IP or hostname to bind server to

# Type of socket to set up
serverSocket = socket(AF_INET,SOCK_DGRAM)
# Set up the listener
serverSocket.bind((serverHostIP,serverPort))
print 'The server is ready to receive'

# Loop which listens for data from a client.
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('utf-8').upper().encode('utf-8')
    serverSocket.sendto(modifiedMessage, clientAddress)
