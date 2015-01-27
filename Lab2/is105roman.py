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



def addRoman(left, right):
    newString = left + right
    print newString
    return implodeRoman(newString)

def subtractRoman(left, right):
    left = explodeRoman(left)
    right = explodeRoman(right)
    if len(left) < len(right):
        print "This would result in a negative number. Aborting"
        return -1
    print left, right
    result = left[0:-(len(right))]
    return result

def multiplyRoman(left, right):
    left = explodeRoman(left)
    right = explodeRoman(right)
    result = '' 
    i = 1
    while i <= len(right):
        result += left
        i += 1
    return implodeRoman(result)


def divideRoman(left, right):
    left = explodeRoman(left)
    right = explodeRoman(right)
    result = '' 
    
    i = len(left)
    r = len(right)
    # Check if number is even
    if i%r != 0:
        print "The result is not an even number"
        return -1
    # The number of times this loops runs, is the result of the division.
    while i >= r:
        result += 'I'
        i -= r
    return implodeRoman(result)

def explodeRoman(r):
    result = '' 
    i = rpos = 0 
    rlen = len(romanNumeralMap) # Length of romanNumeralMap
    l = len(r)
    d=dict() # Keep number of occurences for each numeral here
    v=dict() # Dictionary that maps numerals to values
    # Put all numerals into a dictionary with the value 0 assigned
    # Also keep a dictionary with how much each numeral is worth in decimal value.
    for numeral, integer in romanNumeralMap:
        d[numeral] = 0
        v[numeral] = integer
    while i < l and rpos < rlen:
        rpos = 0
        for numeral, integer in romanNumeralMap:
            nl = len(numeral)
            found = r.find(numeral, i, nl+i)
            # If a numeral is found, increment it's occurence in the 'd' dictionary once for each occurence.
            if found != -1:
                d[numeral] += 1
                i = found + len(numeral)
    # Now d should hold information about how many occurences there are for each roman numeral
    # Convert into single I's
    for numeral in d:
        result += 'I' * (d[numeral]*v[numeral])
    return result

def implodeRoman(r):
    result = ''
    r = explodeRoman(r)
    numIs = len(r) # How many occurences of I?
    for numeral, integer in romanNumeralMap:
        
        if numIs == 0:
            break;
        while numIs >= integer:
            # 1001
            result += numeral
            numIs -= integer
    return result