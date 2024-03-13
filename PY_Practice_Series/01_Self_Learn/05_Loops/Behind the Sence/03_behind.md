____________________________________________________________________________________________________________________________________________________
# **BEHIND THE SCENE OF OF LOOPS WITH Dictionary:-**
______________________________________________________________________________________________________________________________________________________            
                                                                   iter()
                                                [ITERATION TOOLS]-----------[ITREABLE OBJECT]
                                                (FOR, COMPREHENSIION)       (list,file)
                                                        | next()                 |
                                                        |                        |
                                                        | next()                 |
                                                        |                        |
                                                      [__next__] -----------------
                                

```python
# Dictionary keys iteration example
janak_types = {"key1": "value1", "key3": "value3", "key4": "value4", "key5": "value5"}
for key in janak_types.keys():
    print(key)
```

## Creating an Iterator for Dictionary Keys

```python
# Creating an iterator for dictionary keys

# Dictionary example
janak_types = {"key1": "value1", "key3": "value3", "key4": "value4", "key5": "value5"}

# Creating an iterator for dictionary keys
I = iter(janak_types)

# Displaying the iterator object
I  # Output: <dict_keyiterator object at 0x000001B3917435B0>

# Retrieving and printing the next element
I.__next__()  # Output: 'key1'

# Using next() function to retrieve and print the next element
next(I)  # Output: 'key3'

# Creating another iterator for dictionary keys
iter_d = iter(janak_types)

# Checking if the iterator is the same as the dictionary
iter_d is janak_types  # Output: False
```