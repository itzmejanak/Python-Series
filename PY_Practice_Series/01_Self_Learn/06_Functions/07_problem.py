# 7. Function with *args
#     **Problem:** Write a function that takes a variable number of arguments and returns their sum.

def all_arg(*args):
    count = 0
    for arg in args:
        count += arg

    return count

result = all_arg(1,2,3,3,4,4,5,5)
print(result)