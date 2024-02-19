# STRINGS SLICING AND DICEING :-
# Define a string
janak = "janak"

# Print the string
print(janak)  # Output: 'janak'

# Slice the string to get the first character
slice_janak = janak[0]
print(slice_janak)  # Output: 'j'

# Slice the string to get the first three characters
slice_jan = janak[0:3]
print(slice_jan)  # Output: 'jan'

# Define a string containing numbers
numlist = "123456787654"

# Slice the string to get characters from index 3 to the end
print(numlist[3:])  # Output: '456787654'

# Slice the string to get characters from the start to index 3 (exclusive)
print(numlist[:3])  # Output: '123'

# Slice the string to get characters from index 0 to index 7 with a step of 2
print(numlist[0:7:2])  # Output: '1357'

# Slice the string to get characters from index 0 to index 7 with a step of 3
print(numlist[0:7:3])  # Output: '147'


# STRING METHODS :-

# Define a string
janak = "janak"

# Print the string
print(janak)  # Output: 'janak'

# Call the lower() method to convert the string to lowercase
print(janak.lower())  # Output: 'janak'

# Call the upper() method to convert the string to uppercase
print(janak.upper())  # Output: 'JANAK'

# Define a string with leading and trailing spaces
janak = "             janak boy              "

# Print the string
print(janak)  # Output: '             janak boy              '

# Call the strip() method to remove leading and trailing whitespace
print(janak.strip())  # Output: 'janak boy'

# Assign a new string to the variable janak
janak = "Zaan"

# Call the replace() method to replace a substring
print(janak.replace("Zaan", "Janak"))  # Output: 'Janak'

# The original string remains unchanged
print(janak)  # Output: 'Zaan'



# STRING CONVERSION :-
# Define a string
rex = 'janak, zaan, don, coder, logical'

# Split the string by whitespace (default)
print(rex.split())  # Output: ['janak,', 'zaan,', 'don,', 'coder,', 'logical']

# Split the string by comma and space
print(rex.split(", "))  # Output: ['janak', 'zaan', 'don', 'coder', 'logical']

# Define a string
janak = "Zaan boy"

# Find the index of the substring "zaan" (case-sensitive)
print(janak.find("zaan"))  # Output: -1 (not found)

# Find the index of the substring "Zaan"
print(janak.find("Zaan"))  # Output: 0 (found at index 0)

# Define a string
janak = "Zaan boy man don bro"

# Count the occurrences of the substring "Zaan"
print(janak.count("Zaan"))  # Output: 1



# String formatting :-
# Define variables
janak_type = "Rex"
quantity = 2
order = "I order {} types of {}"

# Print the initial template string
print(order)  # Output: 'I order {} types of {}'

# Use the format() method to insert values into the template
formatted_order = order.format(quantity, janak_type)
print(formatted_order)  # Output: 'I order 2 types of Rex'


# CONVERSION LIST TO STRING :-
# Define a list
janak_type = ["Rex", "zaan", "hero"]

# Print the list
print(janak_type)  # Output: ['Rex', 'zaan', 'hero']

# Use the join() method to concatenate the elements of the list into a single string
concatenated_string = "".join(janak_type)
print(concatenated_string)  # Output: 'Rexzaanhero'

# Use the join() method with a space separator to concatenate the elements with spaces between them
concatenated_with_spaces = " ".join(janak_type)
print(concatenated_with_spaces)  # Output: 'Rex zaan hero'


# SOME RULES :-
# Iterating over characters in a string
janak = "zaan is best boy"
for letter in janak:
    print(letter)

# Output:
# z
# a
# a
# n
# (newline)
# i
# s
# (space)
# b
# e
# s
# t
# (space)
# b
# o
# y

# Using double quotes inside a string
janak = "he said, \"janak is good boy\""
print(janak)  # Output: 'he said, "janak is good boy"'

# Using newline character (\n) in a string
janak = "zaan\njanak"
print(janak)  # Output:
# zaan
# janak

# Using raw string (r-prefix)
janak = r"zaan\njanak"
print(janak)  # Output: 'zaan\njanak'
print(janak)  # Output: zaan\njanak

# Using raw string for Windows file path
janak = r"c:user\pwd"
print(janak)  # Output: 'c:user\pwd'
print(janak)  # Output: c:user\pwd



# CHECKING THE EXISTANCE OF THE STRINGS :-
janak = "janak is the good boy"

# Check if the substring "good" exists in the string
print("good" in janak)  # Output: True
