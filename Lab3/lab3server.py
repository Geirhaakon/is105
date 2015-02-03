'''
Created on 2. feb. 2015

@author: GGreibesland
'''
from socket import *
from lab3supportmodule import *
import json

serverPort = 12000 # Server port to bind to
serverHostIP = 'localhost' # IP or hostname to bind server to
debug = True


def lab3debug(msg):
    if debug:
        print msg
        

# List of supported functions.
# I created a regular list, because of trouble with converting a MAP to json.
# The list is separated by :
# 1st space is for the command
# 2nd space is the description of the command
# 3rd space is for command category
supportedFunc = ('v: turn off or on verbose mode:system',
                 'r: do math operations on roman numerals:roman',
                 'u: convert string to uppercase by using the upper function:upper',
                 'b: convert a string to uppercase by manipulating binary representation of character:upper',
                 'd: convert a string to uppercase by manupulating decimal representation of character:upper',
                 'e: exit client program:system',
                 's: shut down server program and exit client:system',
                 'h: show this help text:help')
# List of supported roman functions
# Same idea as the above list.
# 1st space is the function name
# 2nd space is the description
supportedRomanFunc = ('toInt:Convert roman to int',
                      'toRoman:Convert int to roman',
                      'add:Add two roman numerals',
                      'subtract:Subtract two roman numerals',
                      'mult:multiply two roman numerals',
                      'divide:divide two roman numerals')



# Type of socket to set up
serverSocket = socket(AF_INET,SOCK_DGRAM)
# Set up the listener
serverSocket.bind((serverHostIP,serverPort))
print 'The server is ready to receive'

def startServer():
    # Loop which listens for data from a client.
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        messagefromClient = decodeData(json.loads(message))
        
        decodedMessage = messagefromClient[1]
        command = messagefromClient[0] #.decode('utf-8')
        lab3debug('Message from client is: ' + message)
        lab3debug('Command is:' + command)
        
        if command == unicode('system') and decodedMessage == unicode('getFunctions'):
            reply = json.dumps(supportedFunc)
        if command == unicode('system') and decodedMessage == unicode('shutdown'):
            print 'Exiting server application'
            break
        if command == unicode('u'):
            reply = decodedMessage.upper() #.encode('utf-8')
            reply = json.dumps(encodeData((reply)))
        if command == unicode('d'):
            charReply = reply = ''
            for l in decodedMessage:
                reply += chr(charToUpperDec(l))
                charReply += str(charToUpperDec(l)) + ' '
            reply = json.dumps(encodeData((reply, charReply)))
        if command == unicode('b'):
            charReply = binReply = reply = ''
            for l in decodedMessage:
                reply += chr(charToUpperBin(l))
                charReply += str(charToUpperBin(l)) + ' '
                binReply += unicodeBin(chr(charToUpperBin(l))) + ' '
            reply = json.dumps(encodeData((reply, charReply, binReply)))
            
        # Roman functions
        if command == unicode('r'):
            reply = json.dumps(supportedRomanFunc)
            
            # Entery a new loop where we accept only roman commands

        lab3debug('Message to client: ' + reply)
        serverSocket.sendto(reply, clientAddress)



startServer()