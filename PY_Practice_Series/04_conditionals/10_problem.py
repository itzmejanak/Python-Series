# 10. Pet Food Recommendation :-

print("\nChoose your pet from here\n1. Dog\n2. Cat\n")
input_num = int(input("Choose the number from here ? "))

if input_num == 1:
    age = int(input("input your dog age ? "))
    if age <= 2:
        print("Buy Puppy food fro him")
    elif age >= 2 and age <= 7:
        print("Buy Adult dog food fro him")
    elif age > 7:
        print("Buy Senior dog food for him")
elif input_num == 2:
    age = int(input("input your cat age ? "))
    if age <= 1:
        print("Buy baby cat food fro him")
    elif age >= 1 and age <= 5:
        print("Buy Adult cat food fro him")
    elif age > 5:
        print("Buy Senior cat food for him")
else:
    print("Invalid input! ")