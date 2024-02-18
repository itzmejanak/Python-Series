#RAW CODE INTO PY TERMINAL

#>>> username = "janak" 
# >>> len(username) 
# 5   

# for findings the specific part of the string bucasue in python strings aslo treated as array
# >>> username[0] 
# 'j' 

# we cannot change the reference of string so we see error
# >>> username[0] = "J" 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

# start to show from behind
# >>> username[-1]     
# 'k' 

# it help to select the range to print
# >>> username[1:3]
# 'an'

# it helps to show us all avaiable methods for our strings
# >>> dir(username) 
# output here :



#PROPER CODE HERE

# Define the username variable
username = "janak"

# Find the length of the username
print(len(username))  # Output: 5

# Retrieve the first character of the username
print(username[0])  # Output: 'j'

# Attempt to assign a new value to the first character (which will raise an error)
try:
    username[0] = "J"
except TypeError as e:
    print(e)  # Output: 'str' object does not support item assignment

# Retrieve the last character of the username
print(username[-1])  # Output: 'k'

# Retrieve a substring from index 1 to index 2 (exclusive)
print(username[1:3])  # Output: 'an'

# List available attributes and methods of the username string
print(dir(username))
