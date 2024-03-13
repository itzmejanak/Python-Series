____________________________________________________________________________________________________________________________________________________
# **BEHIND THE SCENE OF OF LOOPS WITH LIST:-**
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
# Creating a list
l1 = [1, 2, 3, 4, 5, 6]

# Creating an iterator
I = iter(l1)

# Displaying the memory reference of the list
I  # <list_iterator object at 0x0000020670EBEE60>

# Retrieving and printing the next element
I.__next__()  # 1

# memory reference of the list which dosen't change
I  # <list_iterator object at 0x0000020670EBEE60>

# Subsequent calls to retrieve and print the next elements
I.__next__()  # 2
I.__next__()  # 3
I.__next__()  # 4
I.__next__()  # 5
I.__next__()  # 6

# Attempting to retrieve next element beyond the end of the iterator
I.__next__() # output is StopIteration all list is already been itetrate
```

## Understanding Files and Iterators
```markdown
```python
# File f and iter(f) are the same but not for lists

# File example
f = open("01_problem.py")
iter_f = iter(f)
iter_f is f  # Output: True
```

## Understanding Lists and Iterators


```python
# List l1 and iter(l1) are not the same

# List example
l1 = [1, 2, 3, 4, 5, 6]
iter_l1 = iter(l1)
iter_l1 is l1  # Output: False
```
