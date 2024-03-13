def add_numInto_list():
    print("\n\tPleaase enter the Number to add it into list from [] and end []")
    numbersStart = int(input("\n\tFrom Where you want to store: "))
    numberEnd = int(input("\n\tMention here the end point: \n"))

    listNumbers = []
    listNumbersSqr = []
    evens_nums =[]
    odd_nums = []
    for num in range(numbersStart, numberEnd+1):
        listNumbers.append(num)

    print("Non Square numbers are: ", listNumbers)

    for newnum in listNumbers:
        sqr = newnum**2
        listNumbersSqr.append(sqr)

    print("Square number are: ", listNumbersSqr)

    for even in listNumbersSqr:
        if even % 2 == 0:
            evens_nums.append(even)
    print("Even number are: ", evens_nums)

    for odd in listNumbersSqr:
        if odd % 2 != 0:
            odd_nums.append(odd)
    print("Odd number are: ", odd_nums)

    # for sum of the all list numbers
    print("Sum of Non Square numbers: ", sum(listNumbers))
    print("Sum of Square numbers: ", sum(listNumbersSqr))
    print("Sum of even numbers: ", sum(evens_nums))
    print("Sum of odd numbers: ", sum(odd_nums))

    # for displaying max and min value
    max_number = listNumbers[0]
    min_number = listNumbers[0]
    for num in listNumbers:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
    print("Max number: ", max_number)
    print("Min numbers: ", min_number)

add_numInto_list()