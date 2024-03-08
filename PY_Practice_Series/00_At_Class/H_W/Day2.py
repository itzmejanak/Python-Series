# Q1. WAP that would calculate the price of rent the guest has to pay for a room. Cost
# should be calculated as Rs. 5000 per week or Rs. 1000 per day. Eg. If user wants to
# rent for 10 days, the total should be Rs. 8000 (Rs.5000 for a week and 3000 for
# remaining 3 days) and so on.

# Ask for how many days the guest wants to rent the room for and show the total bill.
# The program should terminate on user request only.

# ________________________________________ANSWER________________________________________

def calculate_rent():
    # Displaying information to the user
    print("\n\tWelcome to Room Rent Calculator!")
    print("-----------------------------------------")
    print("Please provide the following details to proceed:\n")

    # Creating a flag to control the while loop
    exit_requested = False

    # Loop continues until the user decides to exit
    while not exit_requested:
        # Asking the user to provide the number of days
        asked_days = float(input("How many days do you want to book this room? "))

        # Checking if the input is valid
        if asked_days < 1:
            print("\nPlease enter a valid number of days")
            print("---------------------------------")
        else:
            # Assigning the value of the weekly rent and per-day rent
            room_price1 = 5000  # Weekly rent
            room_price2 = 1000  # Per-day rent

            # Calculating the number of full weeks and remaining days
            weeks = asked_days // 7  # only weeks
            remainder_days = asked_days % 7

            # Calculating rent based on weekly and daily rates
            rent1 = weeks * room_price1  # Rent for full weeks
            rent2 = remainder_days * room_price2  # Rent for remaining days

            # Calculating total rent
            total_rent = rent1 + rent2
            print("Total rent is Rs:", total_rent)

            # Asking the user if they want to quit
            choice = input("Do you want to quit? \"Y/N\": ").lower()
            if choice == "y":
                exit_requested = True

# Calling the function to execute the program
calculate_rent()





# Q2. Solve one problem from the book referred from chapter 2 or 5 or 7!

# Rental Car (Task 7-1):
def rental_car():
    car_choice = input("What kind of rental car would you like? ")
    print(f"Let me see if I can find you a {car_choice}.")

rental_car()



# Restaurant Seating (Task 7-2):
def restaurant_seating():
    group_size = int(input("How many people are in your dinner group? "))
    if group_size > 8:
        print("I'm sorry, you'll have to wait for a table.")
    else:
        print("Your table is ready.")

restaurant_seating()



# Multiples of Ten (Task 7-3):
def multiples_of_ten():
    number = int(input("Please enter a number: "))
    if number % 10 == 0:
        print(f"{number} is a multiple of 10.")
    else:
        print(f"{number} is not a multiple of 10.")

multiples_of_ten()
