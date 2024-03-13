# 3. Polymorphism in Functions
# **Problem:** Write a function `multiply` that multiplies two numbers, but can also accept and multiply strings.

def multiply(x, y, z):
    a = int(z)
    print(x * y * a)
multiply(3, 4, "5")