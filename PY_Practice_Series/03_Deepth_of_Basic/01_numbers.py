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

# Concatenation of two strings
print('jan' + 'ak')  # Output: 'janak'
