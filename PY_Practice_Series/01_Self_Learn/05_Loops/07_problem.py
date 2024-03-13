# 7. Validate Input

input_num = int(input("Enter your number "))

while input_num >= 11:
    inp = int(input("Again Enter your number "))
    print("your number is: ", inp)
    if inp < 11 and inp > 0:
        print("Thank you")
        break