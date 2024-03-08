# a = True and False
# b = 0 and True
# c = 1 and 'sam'
# d = 'sam' and 1
# e = 0 and 3
# f = None or 2
# # print(a)
# # print(f)
# print(a,b,c,d,e,f)


def main():
    quit_program = True
    while quit_program:
        print("\t1. Run the program \n\t2. Exit")
        choice = int(input("Choose what you want: "))

        if choice < 1 or choice > 2:
            print("Invalid input")
        elif choice == 1:
            inp1 = int(input("Enter first number: "))
            inp2 = int(input("Enter second number: "))

            if inp1 > inp2:
                m,n = inp1,inp2
            else:
                m,n = inp2,inp1
            
            check = True
            while check:
                r = m % n
                if(r==0):
                    print("HCF is, ", n)
                    check = False
                else:
                    m,n = n,r
        elif choice == 2:
            print("Thank you")
            quit_program = False

if __name__ == "__main__":
    main()




