# 8. Prime Number Checker
inp_num = int(input("Enter your number ?: "))
is_prime = True
if inp_num > 1:
    for inp in range(2, inp_num):
        if (inp_num % inp) == 0:
            is_prime = False
            break
if is_prime:
    print(inp_num, "number is prime number")
else:
    print(inp_num, "number is not prime number")