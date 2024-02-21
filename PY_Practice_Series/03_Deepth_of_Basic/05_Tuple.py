# TUPLE BASIC INFORMATION :-

# Define a tuple of colors
colors = ("yellow", "red", "green", "blue", "orange", "white")

# Print the tuple
print(colors)
# Output: ('yellow', 'red', 'green', 'blue', 'orange', 'white')

# Access the first element of the tuple
print(colors[0])
# Output: 'yellow'

# Access the last element of the tuple using negative indexing
print(colors[-1])
# Output: 'white'

# Access a slice of elements from index 1 to 4 (excluding 5)
print(colors[1:5])
# Output: ('red', 'green', 'blue', 'orange')

# Access all elements of the tuple using slicing
print(colors[:])
# Output: ('yellow', 'red', 'green', 'blue', 'orange', 'white')

# Attempt to assign a new value to the first element (will raise a TypeError)
# Tuple objects do not support item assignment
# colors[0] = "hot pink"

# Find the length of the tuple
print(len(colors))
# Output: 6

# Define another tuple of colors
more_colors = ("crimson", "gray")

# Concatenate both tuples to create a new tuple
all_colors = colors + more_colors

# Print the combined tuple
print(all_colors)
# Output: ('yellow', 'red', 'green', 'blue', 'orange', 'white', 'crimson', 'gray')





# TUPLE WITH CONDITION :-

# Define a tuple of colors
colors = ("yellow", "red", "green", "blue", "orange", "white")

# Check if "yellow" is in the tuple
if "yellow" in colors:
    print("I have yellow color")
# Output: I have yellow color

# Define another tuple with repeated "red" elements
other = ("red", "red")

# Concatenate both tuples to create a new tuple
all_colors = colors + other

# Print the combined tuple
print(all_colors)
# Output: ('yellow', 'red', 'green', 'blue', 'orange', 'white', 'red', 'red')

# Count the occurrences of "red" in the tuple
print(all_colors.count("red"))
# Output: 3

# Count the occurrences of "black" in the tuple
print(all_colors.count("black"))
# Output: 0



# USING TUPLE FOR UNWRAPPING TUPLE :-

# Define a tuple
my_tuple = (10, 20, 30)

# Unpack the tuple into individual variables
a, b, c = my_tuple

# Print the values of the variables
print("a:", a)  # Output: a: 10
print("b:", b)  # Output: b: 20
print("c:", c)  # Output: c: 30
