# dictainory is all about key value pair like obect in JS
# >>> myD = {"one": 'leamon', "two": 'janak', "three": 'comic'} 


# >>> myD
# {'one': 'leamon', 'two': 'janak', 'three': 'comic'}


# we cannot access like this
# >>> myD.one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'one'


# also we cannot access key by giving value
# >>> myD["janak"] 
# Traceback (most recent call last):   
#   File "<stdin>", line 1, in <module>
# KeyError: 'janak'


# we only access this dict by using key
# >>> myD["one"]   
# 'leamon'


# PROPER CODE 
# Define a dictionary named myD
myD = {"one": 'leamon', "two": 'janak', "three": 'comic'}

# Print the dictionary
print(myD)  # Output: {'one': 'leamon', 'two': 'janak', 'three': 'comic'}

# Attempt to access a key using dot notation (which will raise an AttributeError)
try:
    print(myD.one)
except AttributeError as e:
    print(e)  # Output: 'dict' object has no attribute 'one'

# Attempt to access a key that does not exist (which will raise a KeyError)
try:
    print(myD["janak"])
except KeyError as e:
    print(e)  # Output: 'janak'

# Access a key that exists in the dictionary
print(myD["one"])  # Output: 'leamon'
