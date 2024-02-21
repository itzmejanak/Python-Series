# 9. List Uniqueness Checker

tea_varieties = ["coffee", "olang", "green", "black", "white", "coffee", "olang","green"]
duplicate = []
for word in tea_varieties:
    if tea_varieties.count(word) > 1:
        duplicate = duplicate + [word]
print(duplicate)
