'''
Created on 2. feb. 2015

@author: GGreibesland
'''
from socket import *
#from lab3supportmodule import encodeData, decodeData
import json

serverName = 'localhost' # Server to connect to
serverPort = 12000 # Remote server port
clientSocket = socket(AF_INET, SOCK_DGRAM)
global verboseMode 
verboseMode = True

# Receive list of functions from server
def getSupportedFuncFromServer(type):
    if type == 'roman': command = 'getRomanFunctions'
    if type == 'upper': command = 'getUpperFunctions'
    command = json.dumps(('system', command), encoding="utf-8")
    clientSocket.sendto(command,(serverName, serverPort))
    result, serverAddress = clientSocket.recvfrom(2048)
    return json.loads(result, encoding="utf-8")

def printSupportedFunc(flist):
    print 'This application supports %i commands:' % len(flist)
    for f in flist:
        cmd = f.split(':')
        print cmd[0] + ':\t', cmd[1]

def getSupportedFuncCommands(flist):
    funcs = []
    i=0
    for f in flist:
        func = f.split(':')
        if i != len(flist):
            funcs.append(func[0])
        i += 1
    return funcs

def getCommandCategoryMap(lists):
    d = dict()
    for lst in lists:
        for cmd in lst:
            c = cmd.split(':')
            # Map between command name c[0] and it's category c[2]
            d[c[0]] = c[2]
    return d


""" Ask the user for something, return message """
def getUserInput(msgToUser):
    # Ask user for input, decode
    message = raw_input(msgToUser)
    message = message.decode('utf8')
    return message


""" Send something to server, receive something back, return """
def talkToServer(fun, message):
    # Prepend the function to run in the message followed by a colon
    message = json.dumps((fun, message), encoding="utf-8")
    clientSocket.sendto(message,(serverName, serverPort))
    msgFromServer, serverAddress = clientSocket.recvfrom(2048)
    jsonFromServer = json.loads(msgFromServer, encoding="utf-8")
    return jsonFromServer


""" Convert a lowercase string to uppercase
    Supports converting via:
    sting.upper()
    subtracting 32 from character ordinal
    Modifying binary representation of character ordinal
"""
def upperConvert(fun):
    lowerc = getUserInput('Input lowercase sentence:')
    if lowerc.istitle():
        print 'Whoops! Only lowercase characters are supported'
        return
    jsonFromServer = talkToServer(fun, lowerc)
    printServerReply('Characters in uppercase: ','')
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
        
        
""" Print a reply from server.
    two parameters:
    replymsg: message to show user
    data: data from server to show
"""
def printServerReply(replymsg, data):            
    print '==========================\nReply from server:'
    print replymsg, 
    print unicode(data)

""" This function handles the roman functions of this application """
def roman(fun):
    # Show available functions
    printSupportedFunc(supportedRomanFunc)
    while True:
        fun = getCommandFromUser(supportedRomanFunc)
        # Some special commands, like exit, shutdown and help
        if fun == 'e': break
        elif fun == 'h': printSupportedFunc(supportedRomanFunc)
        
        # Roman functions
        elif fun == 'toInt':
            jsonFromServer = talkToServer(fun, getUserInput('Input roman Numeral:'))
            printServerReply('Numeral value: ', jsonFromServer)
        elif fun == 'toRoman':
            jsonFromServer = talkToServer(fun, getUserInput('Input an integer:'))
            printServerReply('Roman value: ', jsonFromServer)
        elif fun in ('add', 'subtract', 'mult', 'divide'):
            userInput = getUserInput('Input two roman numerals separated by a space:').split()
            if len(userInput) == 2 and isinstance(userInput, list):
                jsonFromServer = talkToServer(fun, (userInput))
                printServerReply('Result: ', jsonFromServer)
            else:
                print "This command requires two roman numerals separated by a space."
                print "Example: IV VI"
                
""" Check if a command is valid according to the function list supplied """
def isValidCommand(cmd, flist):
    if cmd in getSupportedFuncCommands(flist):
        return True
    else: 
        return False

def getCommandFromUser(flist):
    # Ask user for command
    #fun = raw_input('Please select which function you want to use (' + ', '.join(getSupportedFuncCommands(flist)) + '): ').decode('utf8').encode('utf8')
    fun = getUserInput('Please select which function you want to use (' + ', '.join(getSupportedFuncCommands(flist)) + '): ')
    # Check if command is valid
    if fun == '':
        print 'Blank command detected, please supply a valid command'
        return
    else:
        splitFun = fun.split()
        if isValidCommand(splitFun[0], flist):
            return fun
        else:
            print 'Sorry, that is not a valid command.'
            return


def sysFunctions(fun):
    # Flip verbose mode
    if fun == 'v':
        global verboseMode
        verboseMode = not verboseMode
        print 'Verbose mode on: ', verboseMode

def shutdownServer():
    message = json.dumps(('system', 'shutdown'), encoding="utf-8")
    clientSocket.sendto(message,(serverName, serverPort))

#Save a list of supported functions for later use
supportedFunc = getSupportedFuncFromServer('upper')
supportedRomanFunc = getSupportedFuncFromServer('roman')
commandCategoryMap = getCommandCategoryMap((supportedFunc,supportedRomanFunc))




# Print welcome and a list of supported commands
print 'Hi, welcome to this lab3 test program.'
printSupportedFunc(supportedFunc)
# Start main program loop
while True:
    
    # Ask user what function to use
    fun = getCommandFromUser(supportedFunc)
    # Some special commands, like exit, shutdown and help
    if fun == 'e': break
    if fun == 's':
        shutdownServer()
        break
    if fun == 'h': printSupportedFunc(supportedFunc)
    
    # Other commands, main functions of the program
    if commandCategoryMap[fun] == 'upper': upperConvert(fun)
    if commandCategoryMap[fun] == 'roman': roman(fun)
    if commandCategoryMap[fun] == 'system': sysFunctions(fun)

    

clientSocket.close()
        
print 'Goodbye'
