# main_list = [[24, 3, 6], [8, 12, 18], [2, 66, 7]]

# def solution(lists):
#     divisible = []
#     for sublist in lists:
#         for number in sublist:
#             if number % 2 == 0:
#                 divisible.append(number)
#     print("Even numbers in each sublist:", divisible)

#     maximum = None  
#     minimum = None 
#     for sublist in lists:
#         for number in sublist:
#             if number % 2 == 0:
#                 if maximum is None or number > maximum:
#                     maximum = number
#                 if minimum is None or number < minimum:
#                     minimum = number
#     print("Maximum even number:", maximum)
#     print("Minimum even number:", minimum)

# solution(main_list)


# def dict_solution():
#     main_dict = []
    
#     input_limit = 0
#     while not input_limit == 5:
#         name = input("Enter your name: ")
#         marks_obtained = int(input("Enter marks obtained: ")) 
#         user_data = {"Name": name, "Marks": marks_obtained}
#         main_dict.append(user_data)
#         input_limit += 1
    
#     print("Data stored successfully!")
    
#     for info in main_dict:
#         print(info)

# dict_solution()


# OR

def dict_solution1():
    main_dict = {}
    
    input_limit = 0
    while not input_limit == 2:
        name = input("Enter your name: ")
        marks_obtained = int(input("Enter marks obtained: ")) 
        user_data = {"Name": name, "Marks": marks_obtained}
        main_dict[name] = user_data
        input_limit += 1
    
    print("Data stored successfully!")

    for name, info in main_dict.items():
        print(f"Name: {name}, Marks: {info['Marks']}")

dict_solution1()


dict_solution1()
