
# Python Scopes and Variables

In Python, scopes define the accessibility of variables. Each indentation level represents a different scope, and variables defined within a scope are accessible only within that scope unless explicitly specified otherwise. Here's a breakdown of Python scopes:

## 1. Global Scope

Variables defined at the top level of a module or declared as global within a function belong to the global scope.

```python
global_var = 10

def global_scope_func():
    print(global_var)

global_scope_func()  # Output: 10
```

## 2. Local Scope (Function Scope)

Variables defined within a function belong to the local scope of that function.

```python
def local_scope_func():
    local_var = 20
    print(local_var)

local_scope_func()  # Output: 20
```

## 3. Enclosing Scope (Nonlocal Scope)

Variables defined in an enclosing function's scope and accessed in nested functions belong to the enclosing scope.

```python
def outer():
    outer_var = 30
    def inner():
        print(outer_var)
    inner()

outer()  # Output: 30
```

## 4. Built-in Scope

Python comes with several built-in functions and exceptions that are accessible in any scope without the need for an import statement.

```python
print(len([1, 2, 3]))  # Output: 3
```

## 5. Comprehension Scope

Variables defined within list comprehensions, dictionary comprehensions, or generator expressions have their own scope.

```python
x = [i for i in range(5)]
print(i)  # NameError: name 'i' is not defined
```

## 6. Class Scope

Variables defined within a class but outside of any method belong to the class scope.

```python
class MyClass:
    class_var = 50

print(MyClass.class_var)  # Output: 50
```

## 7. Instance Scope

Variables defined within methods of a class and accessed using `self` belong to the instance scope.

```python
class MyClass:
    def __init__(self):
        self.instance_var = 60

obj = MyClass()
print(obj.instance_var)  # Output: 60
```

## 8. Conditional Scope

Variables defined within if statements or loops have their own scope.

```python
if True:
    cond_var = 70
print(cond_var)  # Output: 70
```

## 9. Exception Scope

Variables defined within an exception handling block (`try`, `except`, `finally`) have their own scope.

```python
try:
    raise ValueError("An error occurred")
except ValueError as e:
    exc_var = e
print(exc_var)  # Output: An error occurred
```


## 10. Others Scopes
```python
username = "chaiaurcode"

def func():
    username = "chai"
    print(username)

print(username)
func()


x = 99 
def func2(y):
    z = x + y
    return z

result = func2(1)
print(result)

def func3():
    global x
    x = 12
    
func3()
print(x)



def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


# closer 
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual



f = chaicoder(2)   # give parameter for chaiaurcoder()
g = chaicoder(3)

print(f(3))         # give parameter for local actual function
print(g(3))
```

Each of these scopes has its own set of rules for variable accessibility and lifetime. Understanding these scopes is crucial for writing maintainable and bug-free Python code.
