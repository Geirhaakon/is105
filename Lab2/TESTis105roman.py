'''
Created on 27. jan. 2015

@author: GGreibesland
'''

import is105roman
# This file demonstrates how to use is105roman.py, and it tests that the module works correctly.

print '''\
==========================================================
A series of tests will now run.
Some of the tests prints out a message to the terminal,
some of them will be errors.
As long as no assertion errors appear, the test is OK.

==========================================================
An assertion error would look something like this:
/////////////////////////////////////////////////
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
/////////////////////////////////////////////////


Starting tests
==========================================================
'''

# Convert decimal numbers to roman numerals:

assert is105roman.toInt('X') == 10

# Check that it works with lowercase letters

assert is105roman.toInt('x') == 10

# Check that large roman numerals work
 
assert is105roman.toInt('MCMLIV') == 1954 # The last time I saw Paris
assert is105roman.toInt('MMXIV') == 2014

# Check that each roman numeral has the correct decimal Value
assert is105roman.toInt('M') == 1000
assert is105roman.toInt('CM') == 900 
assert is105roman.toInt('D') == 500 
assert is105roman.toInt('CD') == 400 
assert is105roman.toInt('XC') == 90 
assert is105roman.toInt('L') == 50 
assert is105roman.toInt('XL') == 40 
assert is105roman.toInt('X') == 10
assert is105roman.toInt('IX') == 9
assert is105roman.toInt('V') == 5
assert is105roman.toInt('IV') == 4
assert is105roman.toInt('I') == 1


# Negative test, try roman numeral that does not exist
assert is105roman.toInt('A') == -1 # This will also print a message to the console.

# Now let's test from int to roman

# Convert a number to roman numeral
assert is105roman.toRoman(1954) == 'MCMLIV'
assert is105roman.toRoman(2014) == 'MMXIV'

# Negative test, try to use a number with decimal
assert is105roman.toRoman(10.5) == -1 # Will print message to console

# Check that each decimal has the correct roman numeral value
assert is105roman.toRoman(1000) == 'M' 
assert is105roman.toRoman(900) == 'CM'
assert is105roman.toRoman(500) == 'D' 
assert is105roman.toRoman(400) == 'CD'
assert is105roman.toRoman(90) == 'XC'
assert is105roman.toRoman(50) == 'L' 
assert is105roman.toRoman(40) == 'XL'
assert is105roman.toRoman(10) == 'X' 
assert is105roman.toRoman(9) == 'IX'
assert is105roman.toRoman(5) == 'V'
assert is105roman.toRoman(4) == 'IV'
assert is105roman.toRoman(1) == 'I'



# Test addition of roman numbers

assert is105roman.addRoman('V', 'XXXV') == 'XL'


# Test substraction of roman numbers

assert is105roman.subtractRoman('MCMLIV', 'XLIV') == 'MCMX'


# Test that negative return value is not supported (negative test)

assert is105roman.subtractRoman('X', 'MCMLIV') == -1


# Test multiplication of roman numbers

assert is105roman.multiplyRoman('X', 'III') == 'XXX'
assert is105roman.multiplyRoman('X', 'IIII') == 'XL'
assert is105roman.multiplyRoman('I', 'I') == 'I'
assert is105roman.multiplyRoman('I', 'MM') == 'MM'



# Test of division of roman numbers

assert is105roman.divideRoman('X', 'II') == 'V'
assert is105roman.divideRoman('M', 'II') == 'D'

# Negative test, see that we return -1 if the result would not be an even number
assert is105roman.divideRoman('MCMLIV', 'XLIV') == -1


# Test a bit of everything
assert is105roman.toInt(is105roman.addRoman(is105roman.toRoman(1000), is105roman.multiplyRoman('X','V'))) == 1050



# Test the two support functions, implodeRoman and explodeRoman

# ExplodeRoman should take a string of roman numerals and return only as I's
assert is105roman.explodeRoman('MCMLIV') == 'I'*1954

# ImplodeRoman should take a string of ony I's and return a complete roman numeral, neat and tidy.
assert is105roman.implodeRoman('I'*1954) == 'MCMLIV'
print '''\
==========================================================
Testing completed
==========================================================
'''