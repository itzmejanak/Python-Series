# 5. Find the First Non-Repeated Character
name = "janak devkota"
unique_name =""

for char in name:
   if name.count(char) > 1:
      continue
   unique_name = unique_name + char;
print(unique_name)