# 6. Lambda Function
# **Problem:** Create a lambda function to compute the cube of a number.

# variable = lambda parameter: expression
# result = variable(p1, p2)
# print(result) 

inp = int(input("Type here your number: "))
cube = lambda x: x**3
result = cube(inp)
print(result)
