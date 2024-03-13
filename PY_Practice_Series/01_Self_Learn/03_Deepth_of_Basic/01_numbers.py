#THE NUMBERS IS MOST POWERFUL GAME IN PYTHON
#Numbers is not a single obj it it the group of obj


# expression :-
x = 2
y = 3
z = 4

# INTENSION SHOULD BE CLEAR

# Addition of x and y
print(x + y)  # Output: 5

# This is not good practice
print(x + y * z)  # Output: 14

# This is good practice
print((x + y) * z)  # Output: 20

# This is also good practice
print(x + (y * z))  # Output: 14

# INTENSION SHOULD BE CLEAR

# This is also not good practice
print(40 + 2.23)  # Output: 42.23

# This is good practice
print(40 + int(2.23))  # Output: 42

# This is also good practice
print(40 + float(40))  # Output: 80.0

# Concatenation of two strings / operation overloding
print('jan' + 'ak')  # Output: 'janak'


# Assigning values to variables
x = 2
y = 3
z = 4

# Printing values of x, y, z
print("Values of x, y, z:", x, y, z)
# Performing arithmetic operations and printing the results
print("x + 1 =", x + 1)  # Output: x + 1 = 3
print("y * 2 =", y * 2)  # Output: y * 2 = 6
# Calculating remainders and printing the results
print("y % 2 =", y % 2)  # Output: y % 2 = 1
print("x % 2 =", x % 2)  # Output: x % 2 = 0
# Calculating squares and printing the results
print("x ** 2 =", x ** 2)  # Output: x ** 2 = 4
print("y ** 2 =", y ** 2)  # Output: y ** 2 = 9


# Calculating the result of 1 divided by 3 as a floating-point number
result = 1/3.0
print(result)  # Output: 0.3333333333333333

# Getting the representation of the string "janak"
print(repr("janak"))  # Output: "'janak'"

# Getting the string representation of the string "janak"
print(str("janak"))   # Output: 'janak'

# Printing the string "janak"
print('janak')         # Output: janak


# COMPARISION :-

# Normal comparision
# Less than comparison
print(1 < 2)  # Output: True

# Equality comparison
print(5.0 == 5.0)  # Output: True

# Inequality comparison
print(4.0 != 5.0)  # Output: True



# CHAINED COMPARISION :-
x = 2
y = 3
z = 4

# Displaying the values of x, y, and z
print(x, y, z)  # Output: 2 3 4

# Chained comparison: x < y < z
print(x < y < z)  # Output: True

# Equivalent to: x < y and y < z
print(x < y and y < z)  # Output: True

# Chained comparison: 1 == 2 < 3
print(1 == 2 < 3)  # Output: False

# Equivalent to: 1 == 2 and 2 < 3
print(1 == 2 and 2 < 3)  # Output: False



# USING SOME MODULE OF MATH :-
import math

# Floor of 3.5
print(math.floor(3.5))  # Output: 3

# Floor of -3.5
print(math.floor(-3.5))  # Output: -4

# Truncate of 2.8
print(math.trunc(2.8))  # Output: 2

# Truncate of -2.8
print(math.trunc(-2.8))  # Output: -2


# UNDERSTANDING IMAGINERY NUMBERS CASE INTO PYTHON :-

# Complex number addition: 2 + 1j
print(2 + 1j)  # Output: (2+1j)

# Complex number multiplication: (2+1j) * 3
print((2 + 1j) * 3)  # Output: (6+3j)


# DECIMAL NUMBERS :-
# i. Octal literal: 0o20
octal_number = 0o20  # Equivalent to 2*8^1 + 0*8^0 = 16
print(octal_number)  # Output: 16

# ii. Hexadecimal literal: 0xff
hexadecimal_number = 0xff  # Equivalent to 15*16^1 + 15*16^0 = 255
print(hexadecimal_number)  # Output: 255

# iii. Binary literal: 0b1000
binary_number = 0b1000  # Equivalent to 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0 = 8
print(binary_number)  # Output: 8


#OBTAINGING ANY LITRALS NUMBERS USING SOME METHODS :-
# Convert 17 to octal
octal_representation = oct(17)  # '0o21' - 17 in octal is 21
print(octal_representation)  # Output: '0o21'

# Convert 17 to hexadecimal
hexadecimal_representation = hex(17)  # '0x11' - 17 in hexadecimal is 11
print(hexadecimal_representation)  # Output: '0x11'

# Convert 17 to binary
binary_representation = bin(17)  # '0b10001' - 17 in binary is 10001
print(binary_representation)  # Output: '0b10001'


# Using shortHand way for value literals conversion :-
# Convert 64 to an integer
integer_value = int(64)
print(integer_value)  # Output: 64

# Convert '64' from octal to an integer
octal_integer_value = int('64', 8)  # '64' in octal is equivalent to 52 in decimal
print(octal_integer_value)  # Output: 52

# Convert '10000' from binary to an integer
binary_integer_value = int('10000', 2)  # '10000' in binary is equivalent to 16 in decimal
print(binary_integer_value)  # Output: 16



# BITWISE OPERATION :-
x = 1  # Binary representation: 0001

# Left shifting x by 2 positions
result = x << 2  # Shifting 0001 to the left by 2 positions: 0100
print(result)  # Output: 4

# Bitwise OR operation between x and 2
result_or = x | 2  # 0001 | 0010 = 0011 (binary), which is 3 in decimal
print(result_or)  # Output: 3

# Bitwise AND operation between x and 2
result_and = x & 2  # 0001 & 0010 = 0000 (binary), which is 0 in decimal
print(result_and)  # Output: 0



# RANDOM :-
import random

# Generate a random float between 0 and 1
random_float = random.random()
print(random_float)  # Output: 0.1787736488746172

# Generate a random integer between 1 and 100 (inclusive)
random_integer = random.randint(1, 100)
print(random_integer)  # Output: 93

# Generate another random integer between 1 and 100 (inclusive)
random_integer_2 = random.randint(1, 100)
print(random_integer_2)  # Output: 47

# Define a list
l1 = ["janak", "usha", "rajan"]

# Choose a random element from the list
random_choice = random.choice(l1)
print(random_choice)  # Output: 'janak'

# Choose another random element from the list
random_choice_2 = random.choice(l1)
print(random_choice_2)  # Output: 'usha'

# Shuffle the list in place
random.shuffle(l1)
print(l1)  # Output: ['rajan', 'janak', 'usha']


# Some Dicimal Problems :-
# Floating-point arithmetic
print(0.1 + 0.1 + 0.1)       # Output: 0.30000000000000004
print(0.1 + 0.1 + 0.1 - 0.3)  # Output: 5.551115123125783e-17
print((0.1 + 0.1 + 0.1) - 0.3)  # Output: 5.551115123125783e-17

# note so always use decimal library while working to decimal value into python

# Decimal arithmetic
from decimal import Decimal
result = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")
print(result)  # Output: Decimal('0.0')


# FRACTIONS :-
from fractions import Fraction

# Create a Fraction object with numerator 2 and denominator 7
myfra = Fraction(2, 7)

# Display the Fraction object
print(myfra)  # Output: Fraction(2, 7)


# SET OPERATIONS :-

# Define a set
setone = {1, 2, 3, 4}

# Intersection of setone and {1, 3}
intersection = setone & {1, 3}
print(intersection)  # Output: {1, 3}

# Union of setone and {1, 5}
union2 = setone | {1, 5}
print(union2)  # Output: {1, 2, 3, 4, 5}

# Difference between setone and itself
difference = setone - {1, 2, 3, 4}
print(difference)  # Output: set()


# BOOLEAN OPERATIONS :-

# Checking the type of True
print(type(True))  # Output: <class 'bool'>

# Comparison between 0 and False
print(0 == False)  # Output: True

# Identity comparison between True and 1
print(True is 1)  # Output: False

# Addition of True and 1
print(True + 1)  # Output: 2
