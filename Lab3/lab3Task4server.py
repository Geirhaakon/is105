'''
Created on 2. feb. 2015

@author: GGreibesland
'''
from socket import *

serverPort = 12000 # Server port to bind to
serverHostIP = 'localhost' # IP or hostname to bind server to



def bitAnd(x, y):
    return x&y

def bitXor(x, y):
    return x^y

'''
Input c: a character
It gets converted to uppercase by substracting 32 from its
decimal position in the ascii table
Returns decimal position of uppercase character
'''
def charToUpperDec(c):
    return ord(c) - 32

def charToUpperBin(c):
    return bitXor(ord(c), 32)

def unicodeBin(character):
    return '{0:08b}'.format(ord(character.decode('utf8')))

# Type of socket to set up
serverSocket = socket(AF_INET,SOCK_DGRAM)
# Set up the listener
serverSocket.bind((serverHostIP,serverPort))
print 'The server is ready to receive'

# Loop which listens for data from a client.
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodedMessage = message.decode('utf-8')
    splitMessage = decodedMessage.split(':')
    if splitMessage[0] == unicode('u'):
        reply = splitMessage[1].upper().encode('utf-8')
    if splitMessage[0] == unicode('d'):
        charReply = reply = ''
        for l in splitMessage[1]:
            reply += chr(charToUpperDec(l))
            charReply += str(charToUpperDec(l)) + ' '
        reply = 'Characters in uppercase: ' + reply + '.\nDecimal position in uppercase: ' + charReply
    if splitMessage[0] == unicode('b'):
        charReply = binReply = reply = ''
        for l in splitMessage[1]:
            reply += chr(charToUpperBin(l))
            charReply += str(charToUpperBin(l)) + ' '
            binReply += unicodeBin(chr(charToUpperBin(l))) + ' '
        reply = 'Characters in uppercase: ' + reply + '.\nDecimal position in uppercase: ' + charReply + '\nBinary representation in uppercase: ' + binReply
    serverSocket.sendto(reply, clientAddress)

