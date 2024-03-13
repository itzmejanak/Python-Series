# 10. Recursive Function
# **Problem:** Create a recursive function to calculate the factorial of a number.
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n times factorial of (n-1)
    else:
        return n * factorial(n-1)

print(factorial(5))


# AT THE BEHIND

# factorial(5) calls factorial(4).
# factorial(4) calls factorial(3).
# factorial(3) calls factorial(2).
# factorial(2) calls factorial(1)


# note that :-
# this call only sigle time:-
# print(factorial(5))