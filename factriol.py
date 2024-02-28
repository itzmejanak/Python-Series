# def save_data_helper():
#     num = 9840000000
#     fnum = 9849999999
#     total_numbers = fnum - num + 1
#     with open('youtube.txt', 'w') as file:
#         for i, num in enumerate(range(num, fnum+1), start=1):
#             file.write(str(num) + '\n')
#             progress = i / total_numbers * 100
#             print(f"Progress: {progress:.2f}%  ({i}/{total_numbers} numbers done)", end='\r')
#     print("Progress: 100.00%  (All numbers done)")

# save_data_helper()

while True:
    inp = int(input("write your number ? "))
    fact = 1
    for i in range(1, inp+1):
        fact *= 1
    print (fact)



