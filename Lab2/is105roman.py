romanNumeralMap = (('M', 1000),
                   ('CM', 900),
                   ('D', 500),
                   ('CD', 400),
                   ('XC', 90),
                   ('L', 50),
                   ('XL', 40),
                   ('X', 10),
                   ('IX', 9),
                   ('V', 5),
                   ('IV', 4),
                    ('I', 1))

romanDebug = False


def debug(s):
    if romanDebug:
        print s
        
        
def toRoman(n):
    error = "parameter must be integer, not decimal and in the range of 1 to 4999"
    if not (str(n).isdigit()):
        print error
        return -1
    elif not (0 < n < 5000):
        print error
        return -1 
    result = ""
    for numeral, integer in romanNumeralMap:
        debug(numeral + " " + str(integer))
        while n >= integer:
            result += numeral
            n -= integer
    return result

def toInt(r):
    r = r.upper() # Make everything uppercase
    l = len(r) # Length of the roman number
    # Set result to zero initially
    # Initialize i for while loop, 
    # and Initialize rpos, the current position in romanNumeralMap
    result = i = rpos = 0 
    rlen = len(romanNumeralMap) # Length of romanNumeralMap
    while i < l and rpos < rlen:
        rpos = 0 # reset each iteration
        for numeral, integer in romanNumeralMap:
            debug("Current position in romanNumeralMap: " + str(rpos))
            nl = len(numeral)
            debug("Length of current numeral: " + str(nl))
            found = r.find(numeral, i, nl+i)
            debug("searching for \'" + numeral + "\' in \'" + r[i:nl+i+1] + "\'")
            if found != -1:
                result += integer
                i = found + len(numeral)
                debug("Found " + numeral + ". Setting i to " + str(i) + " and result to " + str(result))
                break
            rpos += 1 #Increment the current position of the romanNumeralMap
            if rpos == rlen:
                print 'Illegal character \'%s\' found' % r[i:nl+i+1]
                return -1
    return result