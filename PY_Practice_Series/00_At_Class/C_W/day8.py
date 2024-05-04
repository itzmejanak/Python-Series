
msg = input("Write you Message: ")
# hello
def vowelsAndCon(msg):
    vowels = ["a","e","i","o","u"]
    countForVowels = 0
    countForCon = 0
    for char in msg:
        
        if char in vowels:
            countForVowels += 1
        else:
            countForCon += 1

        """
            if char in vowels:
                countForVowels += 1
            else:
                countForCon += 1
        """

    print("Vowels count: ",countForVowels)
    print("Consonant count: ",countForCon)

vowelsAndCon(msg)


# counter = 0
#         countForVowels = 0
#         countForCons = 0
#         if char == vowels[counter]:
#             countForVowels += 1
#         if char != vowels[counter]:
#             countForCons += 1
#         counter += 1