'''
Created on 2. feb. 2015

@author: GGreibesland
'''
from socket import *
from lab3supportmodule import encodeData, decodeData
import json

serverName = 'localhost' # Server to connect to
serverPort = 12000 # Remote server port
clientSocket = socket(AF_INET, SOCK_DGRAM)
global verboseMode 
verboseMode = True

# Receive list of functions from server
def getSupportedFuncFromServer():
    command = json.dumps(encodeData(('system', 'getFunctions')))
    clientSocket.sendto(command,(serverName, serverPort))
    result, serverAddress = clientSocket.recvfrom(2048)
    return json.loads(result)

def printSupportedFunc():
    print 'This application supports %i commands:' % len(supportedFunc)
    for f in supportedFunc:
        cmd = f.split(':')
        print cmd[0] + ':\t', cmd[1]

def getSupportedFuncCommands():
    funcs = ''
    i=0
    for f in supportedFunc:
        func = f.split(':')
        if i != len(supportedFunc):
            funcs += func[0] + ', '
        i += 1
    return funcs

def getCommandCategoryMap():
    d = dict()
    for cmd in supportedFunc:
        c = cmd.split(':')
        d[c[0]] = c[2]
    return d

def upperConvert(fun):
    # Ask user for input, decode, encode, then send.
    message = raw_input('Input lowercase sentence:').decode('utf8').encode('utf8')
    # Prepend the function to run in the message followed by a colon
    message = json.dumps(encodeData((fun, message)))
    clientSocket.sendto(message,(serverName, serverPort))
    msgFromServer, serverAddress = clientSocket.recvfrom(2048)
    jsonFromServer = decodeData(json.loads(msgFromServer))
    print '==========================\nReply from server:'
    print 'Characters in uppercase: ',
    if fun == 'u':
        print unicode(jsonFromServer)
    if fun in 'db':
        print jsonFromServer[0]
        if verboseMode:
            print '\nDecimal position in uppercase: ',
            print jsonFromServer[1]
    if fun == 'b' and verboseMode:
        print '\nBinary representation in uppercase: ',
        print jsonFromServer[2]
    
def roman(fun):
    pass

def sysFunctions(fun):
    # Flip verbose mode
    if fun == 'v':
        global verboseMode
        verboseMode = not verboseMode
        print 'Verbose mode on: ', verboseMode

def shutdownServer():
    message = json.dumps(('system', 'shutdown'))
    clientSocket.sendto(message,(serverName, serverPort))

#Save a list of supported functions for later use
supportedFunc = getSupportedFuncFromServer()
commandCategoryMap = getCommandCategoryMap()



# Print welcome and a list of supported commands
print 'Hi, welcome to this lab3 test program.'
printSupportedFunc()
# Start main program loop
while True:
    
    # Ask user what function to use
    fun = raw_input('Please select which function you want to use (' + getSupportedFuncCommands() + '): ').decode('utf8').encode('utf8')
    # Check if command is valid
    if fun in (getSupportedFuncCommands()) and fun != '':
        # Some special commands, like exit, shutdown and help
        if fun == 'e': break
        if fun == 's':
            shutdownServer()
            break
        if fun == 'h': printSupportedFunc()
        
        # Other commands, main functions of the program
        if commandCategoryMap[fun] == 'upper': upperConvert(fun)
        if commandCategoryMap[fun] == 'roman': roman(fun)
        if commandCategoryMap[fun] == 'system': sysFunctions(fun)

        
    else:
        print 'Sorry, that is not a supported command.'

clientSocket.close()
        
print 'Goodbye'