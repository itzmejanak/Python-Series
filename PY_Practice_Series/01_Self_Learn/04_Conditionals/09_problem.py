# 9. Leap Year Checker :-
year = int(input("Which year do you want to check for leap year?.. "))

if year % 4 == 0:
    if year % 100 != 0:
        print("This year is a leap year")
    elif year % 400 == 0:
        print("This year is a leap year")
    else:
        print("This year is not a leap year [in]")
else:
    print("This year is not a leap year [out]")

