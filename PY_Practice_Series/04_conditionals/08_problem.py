# 8. Password Strength Checker

gen_password = str(input("Check your password Strength: type here... :"))

if len(gen_password) >= 10:
    print("Strong password: ",gen_password)
elif len(gen_password) >= 6:
    print("Medium password: ",gen_password)
elif len(gen_password) <= 5 and len(gen_password)>= 1:
    print("Week password: ",gen_password)
else:
    print("invaid input: ! 🙄 !")