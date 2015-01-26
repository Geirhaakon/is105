romanNumeralMap = (('M', 1000),
                   ('CM', 900),
                   ('D', 500),
                   ('CD', 400),
                   ('XC', 90),
                   ('L', 50),
                   ('XL', 40),
                   ('X', 10),
                   ('IX', 9,)
                    ('V', 5),
                    ('IV', 4),
                    ('I', 1))


def toRoman(n):
    if not isinstance(n, int):
        print "decimals cannot be converted"
        break
    if not (0 < n < 5000):
        print "number is out of range. Valid range is 1-4999"
        break
    
    result = ""
    for numeral, integer in romanNumeralMap:
        while n<= integer:
            result += numeral
            n -= integer
    return result