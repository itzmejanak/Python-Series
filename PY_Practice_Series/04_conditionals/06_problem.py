# Transportation Mode Selection
km = int(input("What is the distance in KM?: "))

if km <= 3:
    acty = "Walk"
elif km >= 4 and km <= 14:
    acty = "Bike"
elif km >= 15:
    acty = "Car"

print("AI recommends you the transport of: ", acty)
