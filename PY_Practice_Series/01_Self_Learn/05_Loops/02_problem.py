total_number = int(input("Upto How much even number you want to make sum ? "))
sumnum = 0

for i in range(1, total_number+1):
    if i % 2 == 0:
        sumnum+= i
print("sum of even number is: ", sumnum)
