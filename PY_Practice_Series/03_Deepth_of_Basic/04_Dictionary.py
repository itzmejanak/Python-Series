# Dictionary = Object

# Accesing Dictionary and changing VALUES :-

# Define the initial dictionary
janak_types = {"key1": "value1", "key3": "value3", "key4": "value4", "key5": "value5"}

print(len(janak_types))  # Output will be 4

# Print the initial dictionary
print(janak_types)

# Update the value associated with "key1"
janak_types["key1"] = "Zaan"

# Update multiple values simultaneously
janak_types["key3"], janak_types["key1"], janak_types["key4"], janak_types["key5"] = "zaan", "Good", "man", "Nice"

# Print the updated dictionary
print(janak_types)


# LOOPS IN Dictionary VALUES :-

# Define the dictionary
janak_types = {'key1': 'Good', 'key3': 'zaan', 'key4': 'man', 'key5': 'Nice'}

# Iterate over keys and print them
for zaan in janak_types:
    print(zaan)

# Iterate over keys and print key-value pairs
for zaan in janak_types:
    print(zaan, janak_types[zaan])

# Iterate over key-value pairs using the items() method and print them
for key, value in janak_types.items():  
    print(key, value)



# Dictionary Helper :-
    
# Initialize a dictionary
janak_types = {'key1': 'Good', 'key3': 'zaan', 'key4': 'man', 'key5': 'Nice'}

# Find the length of the dictionary
print(len(janak_types))  # Output: 4

# Add a new key-value pair to the dictionary
janak_types["key6"] = "Hero"

# Print the dictionary to see the changes
print(janak_types)  # Output: {'key1': 'Good', 'key3': 'zaan', 'key4': 'man', 'key5': 'Nice', 'key6': 'Hero'}

# pop() need the parameter which key should be remove
print(janak_types.pop('key1'))  # Output: 'Good'

# Print the dictionary after pop()
print(janak_types)  # Output: {'key3': 'zaan', 'key4': 'man', 'key5': 'Nice', 'key6': 'Hero'}

# popitem() do not need the parameter it will remove last one keyValue
print(janak_types.popitem())  # Output: ('key6', 'Hero')

# Print the dictionary after popitem()
print(janak_types)  # Output: {'key3': 'zaan', 'key4': 'man', 'key5': 'Nice'}

# Delete Alway delete/remove value from the momory
# it is use in :- list Disct and many  more
del janak_types["key4"]

# Print the dictionary after deletion
print(janak_types)  # Output: {'key3': 'zaan', 'key5': 'Nice'}

# Create a copy of the dictionary using copy()
janak_typesCopy = janak_types.copy()

# Print the copied dictionary
print(janak_typesCopy)  # Output: {'key3': 'zaan', 'key5': 'Nice'}


# Dictionary in Dictionary :-

phone_book = {
    'janak': {
        'phone': '555-1234',
        'email': 'janak@example.com'
    },
    'Zaan': {
        'phone': '555-5678',
        'email': 'Zaan@example.com'
    }
}

# Print the phone book dictionary
print(phone_book)

# Find the length of the phone book dictionary
print(len(phone_book)) 

# Access the information related to the contact named 'janak'
print(phone_book["janak"])

# Access the phone number of the contact named 'janak'
print(phone_book["janak"]["phone"])



# Dictionary With some special :-
# Create a dictionary using dictionary comprehension to map each number from 0 to 5 to its square
sqr_num = {x: x**2 for x in range(6)}

print(sqr_num)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Clear the dictionary
sqr_num.clear()

# Print the cleared dictionary
print(sqr_num)
# Output: {}



# Working with Differently set keys and values pair in Dictainary:-

keys = ["zaan", "Good", "Boy"]

value = "janak"

# Create a new dictionary with keys from 'keys' and value 'value'
newDict = dict.fromkeys(keys, value)

# Print the new dictionary
print(newDict)
# Output: {'zaan': 'janak', 'Good': 'janak', 'Boy': 'janak'}

# Create a new dictionary with keys from 'keys' and each key associated with the list 'keys'
newDict = dict.fromkeys(keys, keys)

# Print the new dictionary
print(newDict)
# Output: {'zaan': ['zaan', 'Good', 'Boy'], 'Good': ['zaan', 'Good', 'Boy'], 'Boy': ['zaan', 'Good', 'Boy']}
