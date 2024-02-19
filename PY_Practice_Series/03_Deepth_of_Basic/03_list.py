# list = array



# SLICILG AND ACCESING LSIT :-
# Define a list of tea varieties
tea_varieties = ["coffee", "olang", "green", "black", "white"]

# Print the list
print(tea_varieties)  # Output: ['coffee', 'olang', 'green', 'black', 'white']

# Accessing elements by index
print(tea_varieties[0])  # Output: 'coffee'
print(tea_varieties[-1])  # Output: 'white'

# Slicing the list
print(tea_varieties[0:3])  # Output: ['coffee', 'olang', 'green']
print(tea_varieties[3])  # Output: 'black'

# Modifying an element by index
tea_varieties[3] = "herbal"
print(tea_varieties)  # Output: ['coffee', 'olang', 'green', 'herbal', 'white']

# Replacing multiple elements by slice assignment
tea_varieties[1:2] = "herbal"  # Replaces one element with each character of the string
print(tea_varieties)  # Output: ['coffee', 'h', 'e', 'r', 'b', 'a', 'l', 'green', 'herbal', 'white']

# Resetting the list
tea_varieties = ["coffee", "olang", "green", "black", "white"]

# Replacing elements with a list using slice assignment
tea_varieties[1:2] = ["herbal"]
print(tea_varieties)  # Output: ['coffee', 'herbal', 'green', 'black', 'white']

# Replacing multiple elements with multiple elements using slice assignment
tea_varieties[1:3] = ["herbal", "newHerbal"]
print(tea_varieties)  # Output: ['coffee', 'herbal', 'newHerbal', 'black', 'white']




#Inserting NEW VALUE INTO LIST :-
# Define a list of tea varieties
tea_varieties = ["coffee", "olang", "green", "black", "white"]

# Slice from index 1 to 1 (excludes index 1), resulting in an empty list
print(tea_varieties[1:1])  # Output: []

# Insert elements "test" and "test" at index 1
tea_varieties[1:1] = ["test", "test"]
print(tea_varieties)  # Output: ['coffee', 'test', 'test', 'olang', 'green', 'black', 'white']

# Replace the element at index 1 with elements "test" and "test"
tea_varieties[1:2] = ["test", "test"]
print(tea_varieties)  # Output: ['coffee', 'test', 'test', 'test', 'olang', 'green', 'black', 'white']

# Remove elements at index 1 and 2 (but not 3)
tea_varieties[1:3] = []
print(tea_varieties)  # Output: ['coffee', 'test', 'olang', 'green', 'black', 'white']




# LOOPS WITH LIST :-
# Define a list of tea varieties
tea_varieties = ["coffee", "olang", "green", "black", "white"]

# Loop through the list and print each tea variety
for tea in tea_varieties:
    print(tea)
# Output:
# 'coffee'
# 'olang'
# 'green'
# 'black'
# 'white'

# Check if "olang" is in the list and print a message if it is
if "olang" in tea_varieties:
    print("I have this tea")
# Output: I have this tea

# Verify that the list remains unchanged
print(tea_varieties)
# Output: ['coffee', 'olang', 'green', 'black', 'white']

# Remove the last element from the list using the pop() method
removed_tea = tea_varieties.pop()
print(removed_tea)  # Output: 'white'
print(tea_varieties)  # Output: ['coffee', 'olang', 'green', 'black']

# Remove the element "green" from the list using the remove() method
tea_varieties.remove("green")
print(tea_varieties)  # Output: ['coffee', 'olang', 'black']

# Insert the element "white" at index 1 using the insert() method
tea_varieties.insert(1, "white")
print(tea_varieties)  # Output: ['coffee', 'white', 'olang', 'black']

# Create a copy of the list using the copy() method
new_tea_varieties = tea_varieties.copy()
print(new_tea_varieties)  # Output: ['coffee', 'white', 'olang', 'black']

# Append the element "lemon" to the new list
new_tea_varieties.append("lemon")
print(new_tea_varieties)  # Output: ['coffee', 'white', 'olang', 'black', 'lemon']




# LSIT COMPERHANSION :-
# Define a range object from 0 to 9
print(range(10))  # Output: range(0, 10)

# Assign the range object to variable y
y = range(10)
print(y)  # Output: range(0, 10)

# List comprehension to generate a list of squares of numbers from 0 to 9
sqr_nums = [x**2 for x in range(10)]
print(sqr_nums)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
