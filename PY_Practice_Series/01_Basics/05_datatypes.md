# Overview for revesion
## Object Types / Data Types
- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb') #mechanisim

- Boolean : True, False
- None : None
- Funtions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming

# Understand From here
## Object Types / Data Types in Python

This README provides an overview of various object types or data types available in Python programming language.

## Basic Data Types

- **Number**: Examples include integers (`1234`), floating-point numbers (`3.1415`), complex numbers (`3+4j`), binary numbers (`0b111`), `Decimal()` objects, and `Fraction()` objects.
  
- **String**: Examples include single quoted (`'spam'`), double quoted (`"Bob's"`), byte strings (`b'a\x01c'`), unicode strings (`u'sp\xc4m'`).

- **List**: Ordered collections of items enclosed in square brackets (`[]`). Examples include `[1, [2, 'three'], 4.5]` and `list(range(10))`.

- **Tuple**: Ordered, immutable collections of items enclosed in parentheses `()`. Examples include `(1, 'spam', 4, 'U')` and `tuple('spam')`.

- **Dictionary**: Unordered collections of key-value pairs enclosed in curly braces `{}`. Examples include `{'food': 'spam', 'taste': 'yum'}` and `dict(hours=10)`.

- **Set**: Unordered collections of unique elements. Examples include `set('abc')` and `{'a', 'b', 'c'}`.

- **File**: Represents files on the filesystem. Files can be opened using the `open()` function, specifying the filename and optionally the mode (`'r'` for reading, `'w'` for writing, etc.). Examples include `open('eggs.txt')` and `open(r'C:\ham.bin', 'wb')`.

- **Boolean**: Represents truth values. Can be either `True` or `False`.

- **None**: Represents the absence of a value or a null value.

## Functions, Modules, and Classes

These are all fundamental constructs in Python:

- **Functions**: Defined using the `def` keyword, functions are callable objects.

- **Modules**: Python files containing code that can be imported into other scripts using the `import` statement.

- **Classes**: Blueprints for creating objects with specific attributes and behaviors.

## Advanced Concepts

- **Decorators**: Functions that modify the behavior of other functions.

- **Generators**: Functions that generate a sequence of values lazily, one at a time, using the `yield` keyword.

- **Iterators**: Objects that represent a stream of data, implementing the iterator protocol.

- **Metaprogramming**: Writing code that manipulates other parts of a program as objects during runtime.

These concepts extend the capabilities of Python and enable more sophisticated programming techniques.
