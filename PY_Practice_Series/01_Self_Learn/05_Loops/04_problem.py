# 4. Reverse a String

name = "janak Devkota"
reverse_name = ""

for char in name:
    reverse_name = char + reverse_name
print(reverse_name)




# for i in range(len(name) - 1, -1, -1):
#     reverse_name += name[i]

# print(reverse_name)

# HOW AT ATHE BEHIND ITS WORKS 

# Iteration 1:

# char = 'j'
# reverse_name = char + reverse_name
# reverse_name = 'j' + ''
# reverse_name = 'j'
# Iteration 2:

# char = 'a'
# reverse_name = char + reverse_name
# reverse_name = 'a' + 'j'
# reverse_name = 'aj'
# Iteration 3:

# char = 'n'
# reverse_name = char + reverse_name
# reverse_name = 'n' + 'aj'
# reverse_name = 'naj'
# Iteration 4:

# char = 'a'
# reverse_name = char + reverse_name
# reverse_name = 'a' + 'naj'
# reverse_name = 'anaj'
# Iteration 5:

# char = 'k'
# reverse_name = char + reverse_name
# reverse_name = 'k' + 'anaj'
# reverse_name = 'kanaj'
# Iteration 6:

# char = ' '
# reverse_name = char + reverse_name
# reverse_name = ' ' + 'kanaj'
# reverse_name = ' kanaj'