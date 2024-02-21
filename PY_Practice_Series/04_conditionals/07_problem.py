# 7. Coffee Customization

print("\n1. Small\n2. Medium\n3. Large\n\nADDITIONAL\na. Extra shot\n")
input_choice = int(input("Choose the options: "))
input_extra = bool(input("Do you want to add extra shot: "))

if input_extra == True:
    if input_choice == 1:
        print("you have added small coffee with Extra shot")
    elif input_choice == 2:
        print("you have added medium coffee with Extra shot")
    elif input_choice == 3:
        print("you have added large coffee with Extra shot")
else:
    if input_choice == 1:
        print("you have added only small coffee")
    elif input_choice == 2:
        print("you have added only medium coffee ")
    elif input_choice == 3:
        print("you have added only large coffee ")
    
