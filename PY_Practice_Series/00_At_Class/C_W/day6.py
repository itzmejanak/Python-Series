# def bubble_sort(numbers):
#     n = len(numbers)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#     return numbers


# numbers = [5, 2, 7, 1, 9, 3]
# sorted_numbers = bubble_sort(numbers.copy())
# print("Sorted numbers:", sorted_numbers)





def bubbe_shorts():
    take = True
    numbers = []
    while take:
        list_inpt = int(input("Please enter your numbers : "))
        numbers.append(list_inpt)
        choice = input("C/E: ")
        if choice == "e":
            take = False
    
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(numbers)
bubbe_shorts()