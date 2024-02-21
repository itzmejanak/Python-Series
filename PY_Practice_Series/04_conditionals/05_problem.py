# Weather Activity Suggestion
print("\n1. Sunny\n2. Rainy\n3. Snowy\n")
input_num = int(input("Choose the weather condition: "))

if input_num is 1:
    activity = "It is Sunny. \"Go for a walk.\""
elif input_num is 2:
    activity = "It is Rainy. \"Read a book.\""
elif input_num is 3:
    activity = "It is Snowy. \"Build a snowman.\""
else:
    activity = "Invalid input. \"Choose from the given options.\""

print(activity)
