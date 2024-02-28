# input from the user 
num_one = int(input("Enter your first number:  "))
num_two = int(input("Enter your Second number: "))
print("\n")
def sum(num1, num2):
    sum =  num1 + num2
    diff =  num1 - num2
    return sum, diff

rest = sum(num_one, num_two)
# return gives references for sum
print("Sum of numbers is: ",rest[0])
print("\n")
# return gives reference for diff
print("Difference of number is ", rest[1])


print(help(num_one))
print(type(num_one))
print(type(num_two))
