WORKS DONE INTO PYTHON TERMIANL

>>> print("janak") 
janak

>>> 3+5
8  

>>> "janak"*5
'janakjanakjanakjanakjanak'

>>> score = 100
>>> score
100 

this error comes because we do not create any variable
>>> tea
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
NameError: name 'tea' is not defined 

why we do not use [from somewhere import something] for OS

>> because they are core python module and we use this [from somewhere import something] here because this is our created module. [MOdule = some code that are alrady created by some one or by ourself] which we are using it

>>> import os
>>> os.getcwd()         `getcdw = get current working directory`
'C:\\Users\\janak\\OneDrive\\Desktop\\Python'

# Trying to do loop by not using Indentation [TAB]
>>> for c in "chai":
... print(c) 
  File "<stdin>", line 2
    print(c)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for c in "chai":
...     print(c)
... c
`We get errror we have to use indentation [TAB] for space for print(c)`


# Trying to do loop by using Indentation [TAB]
>>>
>>> for c in "chai":
...     print(c)     
... 
c
h
a
i
`We did't get errror we have to use indentation [TAB] for space for print(c)`