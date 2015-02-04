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
supportedRomanFunc = ('h:Show this helptext:system',
                      'e:Go back to the previous menu:system',
                      'toInt:Convert roman to int:roman',
                      'toRoman:Convert int to roman:roman',
                      'add:Add two roman numerals:roman',
                      'subtract:Subtract two roman numerals:roman',
                      'mult:multiply two roman numerals:roman',
                      'divide:divide two roman numerals:roman')



# Type of socket to set up
serverSocket = socket(AF_INET,SOCK_DGRAM)
# Set up the listener
serverSocket.bind((serverHostIP,serverPort))
print 'The server is ready to receive'

def startServer():
    # Loop which listens for data from a client.
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        messagefromClient = json.loads(message, encoding="utf-8")
        
        decodedMessage = messagefromClient[1]
        command = messagefromClient[0]
        lab3debug('Message from client is: ' + message)
        lab3debug('Command is:' + command)
        
        if command == unicode('system') and decodedMessage == unicode('getUpperFunctions'):
            reply = json.dumps(supportedFunc, encoding="utf-8")
        if command == unicode('system') and decodedMessage == unicode('getRomanFunctions'):
            reply = json.dumps(supportedRomanFunc, encoding="utf-8")
        if command == unicode('system') and decodedMessage == unicode('shutdown'):
            print 'Exiting server application'
            break
        if command == unicode('u'):
            reply = decodedMessage.upper()
            reply = json.dumps((reply), encoding="utf-8")
        if command == unicode('d'):
            charReply = reply = ''
            for l in decodedMessage:
                #print type(l)
                reply += unichr(charToUpperDec(l))
                charReply += str(charToUpperDec(l)) + ' '
                #print type(reply), type(charReply)
            print type(reply)
            reply = json.dumps((reply, charReply), encoding="utf-8")
        if command == unicode('b'):
            charReply = binReply = reply = ''
            for l in decodedMessage:
                reply += unichr(charToUpperBin(l))
                charReply += str(charToUpperBin(l)) + ' '
                binReply += bin(charToUpperBin(l)) + ' '
            reply = json.dumps((reply, charReply, binReply), encoding="utf-8")
            
        # Roman functions
        if command in ('add', 'subtract', 'mult', 'divide'):
            left = decodedMessage[0].upper()
            right = decodedMessage[1].upper()
        elif command in ('toInt', 'toRoman'):
            decodedMessage = decodedMessage.upper()
        if command == unicode('toInt') :
            reply = json.dumps((toInt(decodedMessage)), encoding="utf-8")
        if command == unicode('toRoman') :
            reply = json.dumps((toRoman(decodedMessage)), encoding="utf-8")           
        if command == unicode('add') :
            print messagefromClient
            reply = json.dumps((addRoman(left, right)), encoding="utf-8")
        if command == unicode('subtract') :
            reply = json.dumps((subtractRoman(left, right)), encoding="utf-8")
        if command == unicode('mult') :
            reply = json.dumps((multiplyRoman(left, right)), encoding="utf-8")
        if command == unicode('divide') :
            reply = json.dumps((divideRoman(left, right)), encoding="utf-8")
        lab3debug('Message to client: ' + reply)
        serverSocket.sendto(reply, clientAddress)



startServer()
