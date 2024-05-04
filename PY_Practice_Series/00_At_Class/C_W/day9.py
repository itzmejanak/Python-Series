
# Qn 3
def reverse_check():
    value = input("Enter your Words: ")
    list_value = list(value)
    list_value.reverse()

    string_reverse = "".join(list_value)

    if string_reverse == value:
        print("Your words is palindrome")
    else:
        print("Shit ! not the palindrome")


# reverse_check()



value = input("Enter your Numbers: ")

def numbers_intolist(value):
    if not value.isdigit():
        print("Please enter a valid number.")
        return

    list_value = [int(char) for char in value]

    sum_met = sum(list_value)
    
    print("List of digits:", list_value)
    print("Sum of digits:", sum_met)

# numbers_intolist(value)




# Qn 5

value1 = input("Enter your first words: ")
value2 = input("Enter your second Words: ")

def two_words_common(v1,v2):
    list_of_first_word = list(v1)
    list_of_second_word = list(v2)

    common_val = ""
    for each in list_of_first_word:
        if each in list_of_second_word:
            common_val += each
    print("".join(set(common_val)))

# two_words_common(value1, value2)

