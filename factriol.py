while True:
    inpu = int(input("Which num fac you want ? : "))
    fac = 1

    for i in range(1, inpu + 1):
        fac *= i
    print(fac)

    choice = str(input("Do you want to find again: (yes/no)? "))
    if(choice != "yes"):
        break


