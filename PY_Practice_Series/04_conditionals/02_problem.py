# Movie Ticket Pricing

age = int(input("What is your age? "))
day = input("Which day is today? ")

max_price_for_child = 8
discount = 2
max_price_for_adult = 12

if age <= 18:
    if day.lower() == "wednesday":
        print("The price of the ticket is:", max_price_for_child - discount)
    else:
        print("The price of the ticket is:", max_price_for_child)
elif age >= 19:
    if day.lower() == "wednesday":
        print("The price of the ticket is:", max_price_for_adult - discount)
    else:
        print("The price of the ticket is:", max_price_for_adult)
