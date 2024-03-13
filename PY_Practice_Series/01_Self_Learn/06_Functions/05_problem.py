# 5. Default Parameter Value
# roblem:** Write a function that greets a user. If no name is provided, it should greet with a default name.

name = str(input("what is your name ?: "))
def greeting(name):
    if name != "":
        print("Hello🎅: ", name,"Nameste")
    else:
        print("Hello: UNKNOWN \"Good bye\"")

greeting(name)