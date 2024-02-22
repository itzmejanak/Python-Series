# 9. Generator Function with yield
# **Problem:** Write a generator function that yields even numbers up to a specified limit.
inpt = int(input("What is your limit bro: "))
def firstGen(limit):
    for num in range(2, limit+1, 2):
        yield num

for nums in firstGen(inpt):
    print(nums)