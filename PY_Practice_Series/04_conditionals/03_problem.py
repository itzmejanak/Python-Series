# Grade Calculator
score = int(input("What is your score? "))

if score > 100 or score < 1:
    print("Invalid Score. Score should be between 1 and 100.")
    exit()
else:
    if score >= 90:
        print("Your Grade is: A")
    elif score >= 80:
        print("Your Grade is: B")
    elif score >= 70:
        print("Your Grade is: C")
    elif score >= 60:
        print("Your Grade is: D")
    else:
        print("Your Grade is: E")
