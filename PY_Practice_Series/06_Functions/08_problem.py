# 8. Function with **kwargs
# *Problem:** Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def kwrgs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwrgs(name="Alice", age=30, city="New York")