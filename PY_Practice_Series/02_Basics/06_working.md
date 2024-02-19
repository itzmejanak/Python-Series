* **How Python Allocates Memory**
  - Python dynamically allocates memory when assigning values to variables.
  - Variables are references to memory locations holding the assigned values.
  - Reassigning a variable points it to a new memory location without overwriting the existing one.
  - Python's garbage collector frees memory occupied by unreferenced objects eventually.

* **How Python Frees Up Memory**
  - Python reclaims memory using a garbage collector.
  - The collector deallocates memory from objects with zero references periodically.
  - Though not immediate, Python ensures efficient memory usage over time.

* **Memory Optimization**
  - Python optimizes memory by reusing space for immutable objects.
  - It shares references for identical objects, like integers and strings with the same value.
  - Copy-on-write mechanisms optimize memory when creating copies of mutable objects.

* **Mutable vs. Immutable**
  - In Python, objects are mutable or immutable:
  - Mutable objects can change post-creation, altering the object's state.
  - Immutable objects cannot change post-creation, creating new objects for modifications.


## Changing References

```python
l1 = [1, 2, 3]
l2 = l1       ### Both l1 and l2 point to the same reference
l2[0] = 55    ### Modifying l2 also changes l1
print(l1)     ### Output: [55, 2, 3]
print(l2)     ### Output: [55, 2, 3]

python

p1 = [1, 2, 3]
p2 = p1       ### Both p1 and p2 point to the same reference
p1[0] = 44    ### Modifying p1 also changes p2
print(p1)     ### Output: [44, 2, 3]
print(p2)     ### Output: [44, 2, 3]

    [!NOTE]
    If the same reference is assigned to two different variables, changes made to one affect the other.

python

L1 = [1, 2, 3]
L2 = L1       ### Both L1 and L2 point to the same reference
L2 = [1, 2, 3]  ### L2 is assigned to a new reference
L2[0] = 55    ### Modifying L2 does not change L1
print(L1)     ### Output: [1, 2, 3]
print(L2)     ### Output: [55, 2, 3]

    [!NOTE]
    If different references are assigned to different variables, changes made to one do not affect the other.

Copying

python

h1 = [1, 2, 3]
h2 = h1[0:2]  ### Copy a slice of h1
print(h1)     ### Output: [1, 2, 3]
print(h2)     ### Output: [1, 2]

python

h3 = h1[:]   ### Copy the entire list h1
print(h1)    ### Output: [1, 2, 3]
print(h3)    ### Output: [1, 2, 3]

    [!NOTE]
    Slicing or using the copy module (e.g., copy.copy()) creates a new copy of the list.

Checking References

python

m = [1, 2, 3, 4]
n = m
print(m == n)  ### Output: True (checks the value)
print(m is n)  ### Output: True (checks the memory reference)

    [!NOTE]
    The is operator checks if two variables reference the same memory location.

Distinguishing Between is and ==

python

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  ### Output: True (checks the value)
print(a is b)  ### Output: False (checks the memory reference)

