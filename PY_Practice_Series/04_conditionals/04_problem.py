# Fruit Ripeness Checker

Green = "Unripe"
Yellow = "Ripe"
Brown = "Overripe"

f_name = str(input("What is your fruit name? "))
color = str(input("What is your fruit color? "))

if color.lower() == "green":
    print(f_name, " is: ", Green)
elif color.lower() == "yellow":
    print(f_name, " is: ", Yellow)
elif color.lower() == "brown":
    print(f_name, " is: ", Brown)
else:
    print("Invalid color provided.")
