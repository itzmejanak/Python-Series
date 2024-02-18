```markdown
## Basics

### Printing Strings and Arithmetic Operations

```python
print("janak") 
# Output: janak

3 + 5
# Output: 8  

"janak" * 5
# Output: 'janakjanakjanakjanakjanak'
```

### Variable Assignment

```python
score = 100
score
# Output: 100 
```

### Importing Modules

```python
import os
os.getcwd()
# Output: 'C:\\Users\\janak\\OneDrive\\Desktop\\Python'
```

### Understanding Module Import

```python
import os
# No output, but the os module is imported.
```

## Loops and Indentation

### Correct Indentation for Loop

```python
for c in "chai":
    print(c) 
# Output:
# c
# h
# a
# i
```

### Error Due to Indentation

```python
for c in "chai":
    print(c) 
# Error: IndentationError: expected an indented block after 'for' statement on line 1
```

### Misuse of Indentation

```python
for c in "chai":
    print(c)     
# Output:
# c
# h
# a
# i
```
```

```