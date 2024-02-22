# File Reading Examples
## Using `readline()` Method
```markdown

This README provides examples of reading files in Python using different methods.

                   iter()
[ITERATION TOOLS]-----------[ITREABLE OBJECT]
(FOR, COMPREHENSIION)       (list,file)
        | next()                 |
        | next()                 |
    [__next__] -------------------

```python
# Read file "01_problem.py" line by line using file object

# Open the file
f = open("01_problem.py")

# Read the first line
f.readline()  # '# 1. Counting Positive Numbers :-\n'

# Read the second line
f.readline()  # 'numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]\n'

# Read the third line
f.readline()  # 'positive_number_count = 0\n'

# Read the fourth line
f.readline()  # '\n'

# Read the fifth line
f.readline()  # 'for num in numbers:\n'

# Close the file
f.close()
```

## Using `__next__()` Method

```python
# Read file "01_problem.py" line by line using file object with `__next__` method

# Open the file
f = open("01_problem.py")

# Read the first line
f.__next__()  # '# 1. Counting Positive Numbers :-\n'

# Read the second line
f.__next__()  # 'numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]\n'

# Read the third line
f.__next__()  # 'positive_number_count = 0\n'

# Read the fourth line
f.__next__()  # '\n'

# Read the fifth line
f.__next__()  # 'for num in numbers:\n'

# Read the sixth line
f.__next__()  # 'print("final coun of pos number is: ", positive_number_count)\n'

# Attempting to read beyond the end of the file
# StopIteration:

# Close the file
f.close()
```

## More Examples with `for` Loop and `while` Loop
## `for` Loop
```python
# Using for loop to read file line by line
for line in open("01_problem.py"):
    print(line, end='')
```
## `while` Loop
```python
# Using while loop to read file line by line
f = open("01_behind.py")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
```

`These examples demonstrate various ways of reading files in Python. Choose the method that suits your use case best.`
```
