
# asked_days = 34.98
# room_price1 = 600
# room_price2 = 800

# week = asked_days / 7
# print(week)
# week_value = int(week)
# print(week_value)

# floating_val = week - week_value
# print(floating_val)

# rent1 = week_value * room_price1

# rent2 = floating_val * room_price2
# print("Your rent is: ", rent1 + rent2)

# asked_days = float(input("How many days do you want to book this room? "))
# room_price1 = 5000
# room_price2 = 1000

# remainder_days = asked_days % 7
# print(remainder_days)

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

# Debuggig the list and tuple 
# fruits_list = ['apple', 'banana', 'cherry']
# print(fruits_list)
# managedList = '\n'.join(fruits_list)
# print(managedList,"\n")

# fruits_list_tuple = tuple(fruits_list)
# print(fruits_list_tuple)
# managed = '\n'.join(fruits_list_tuple)
# print(managed)

# infop = {
#     "name": "janalk"
# }
# print(infop["name"])


l1 = ['John', 'Alice', 'Bob', 'Eve']

result_dict = {element: len(element) for element in l1}
print(result_dict)

tuple_list = tuple(result_dict.items())
print(tuple_list)

modified_str = '\n'.join(str(item) for item in tuple_list)
print(modified_str)
