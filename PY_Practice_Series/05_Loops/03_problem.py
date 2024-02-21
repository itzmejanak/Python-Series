# Multiplication Table Printer

maxMultiply = 10
for i in range (1, maxMultiply+1):
    if i == 5:
        continue
    for j in range (1, maxMultiply+1):
        print(i,"x",j,"=", i*j)
    print("\n")