# # QN-3 
name = input("What is your name ? ")
def show_name(name):
    return f"Hello \"{name}\", have a nice day"

print(show_name(name))


# #for check
def returns(*args):
    return args
print(returns(1,2,3,4,5,6,7))

print(type(print()))

#Qn-5

x = int(input("What is the value of x: "))
y = int(input("What is the value of y: "))

def Calculated_expression(x,y):
    return x**3+3*x**2*y+3*x*y**3+y**3
print(Calculated_expression(x,y))

# QN-6
radius = int(input("What is the radius of your circle? "))

def area_circle(r):
    pi = 3.14
    return pi*r**2
print(area_circle(radius))


# QN-7
length = int(input("What is the length of the rectangle?: "))
breath = int(input("What is the breath of the rectangle?: "))

def calculate_ractangle(l,b):
    area =f"The area of the rectangle A = \"{l*b}\""
    peremeter = f"The peremeter of the rectangle A = \"{2*(l+b)}\""
    return area, peremeter

result =  calculate_ractangle(length, breath)
print(result[0])
print(result[1])


# QN-9

num1 = 60
num2 = 40
num1 , num2 = num2 , num1

print("the value of number 1 is: ",num1)
print("The value of number 2 is: ",num2)
