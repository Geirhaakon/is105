'''
Created on 2. feb. 2015

@author: GGreibesland
'''
from socket import *
serverName = 'localhost' # Server to connect to
serverPort = 12000 # Remote server port
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Ask user what function to use
print 'Hi, welcome to this lab3 test program.'
print 'This application supports 3 types of test.'
print 'u: convert string to uppercase by using the upper() function'
print 'b: convert by manipulating binary representation of character'
print 'd: convery by manupulating decimal representation of character'
fun = raw_input('Please select which function you want to use (u, b, d): ')
if fun in ('ubd'):
    # Ask user for input, decode, encode, then send.
    message = raw_input('Input lowercase sentence:')
    # Prepend the function to run in the message followed by a colon
    message = (fun + ':' + message).decode('utf8').encode('utf8')
    clientSocket.sendto(message,(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print modifiedMessage
    clientSocket.close()
else:
    print 'Sorry, that is not a supported command.'
