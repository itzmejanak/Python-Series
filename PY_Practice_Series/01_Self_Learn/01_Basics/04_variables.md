Certainly! Here's your snippet formatted in a `README.md` file without any changes:

```markdown
## What is Mutable and Immutable in Python?

Look at this example:

```python
>>> x = 10
>>> y = x
>>> x
10
>>> y
10

# When we assign x to 25
>>> x = 25
>>> x
25   // x is 25 but
>>> 

# y is still 10
>>> y
10  
```

**Note:**
In Python, everything is treated as an object.

Let's understand the behind the scenes of immutability:
When we create:
```python
username = "janak"
```
And then when we redeclare it:
```python
username = "Zaan"
```
Then `username` points only to `"Zaan"`, but it does not change `"janak"`.
Due to garbage collection, the first reference `"janak"` will be deleted.


Let's understand the behind the scenes of our above practice with `x` and `y`:
- At first, `x` refers to `10`.
- After that, we refer `y` to `x`, where `y` also now refers to `10`.
  Note here [both `x` and `y` are pointing to `10`].
- When we change `x`'s reference to `25`, now `x` starts pointing to the new reference `25`, but `y` still points to `10`.
  [That's why `y`'s value remains the same as given to `x` at the first time].
```