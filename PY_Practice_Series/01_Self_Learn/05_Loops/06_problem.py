# 6. Factorial Calculator

number = 5
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1
print("Factorial number value is: ", factorial)


for i in range(factorial, number+1):
    factorial = factorial * number
    number = number - 1
print("Factorial number value is: ", factorial)
