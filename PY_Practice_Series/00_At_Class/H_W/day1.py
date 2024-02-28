# Write a program which takes the input like a, b , c from the user for finding the quardatic equation of the given input.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

def calculate_equation(a,b,c):
    b_val = -b
    down_val = 2*a
    root_inner = b**2 - 4*a*c
    
    if root_inner < 0:
        root  = (-root_inner)**0.5
        top_minus = b_val - (-root)
        top_plus = b_val + (-root)
        final_minus_value = top_minus/down_val
        final_plus_value = top_plus/down_val
        print("The value of x when (-) is: ", float(final_minus_value))
        print("The value of x when (+) is: ", float(final_plus_value))
    else:
        root  = (-root_inner)**0.5
        top_minus = b_val - root
        top_plus = b_val + root
        final_minus_value = top_minus/down_val
        final_plus_value = top_plus/down_val
        print("The value of x when (-) is: ", float(final_minus_value))
        print("The value of x when (+) is: ", float(final_plus_value))
        
calculate_equation(a,b,c)