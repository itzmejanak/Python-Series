list_one = [1,2,3,3,4,5,6,5,6]
list_two = [1,2,3,4,5,6]
listUn = list_one + list_two
print("The Ununique list is: ", listUn)
final = set(listUn)
shorted_list = sorted(final, reverse=True)

print("final list is: ", final)
print("final list is: ", shorted_list)
shorted_list.reverse()
print("final reverse list is: ", shorted_list)





name =  "my name is janak devekota."

name_list = []

for nam in name:
    if nam == "." or nam == ' ':
        continue
    name_list.append(nam)

print(name_list)
sets = set(name_list)
print(sets)
myString = ''.join(sets)
print(myString)
    
    