kitta_no = input("Enter your kitta no: ")

def transform_data_to_list(filepath = "lab7.txt"):
    with open(filepath, 'r') as files:
        contents = files.read()
    first_split = contents.split("\n")
    # print(first_split)
    list_of_data = []
    for line in first_split:
        if line:
            second_split = line.strip().split(",")
            list_of_data.append(second_split)

    print(list_of_data)
    return list_of_data
transform_data_to_list()


def calculate_discount(kitta):
    datas = transform_data_to_list(filepath = "lab7.txt")
    total = 0
    for data in datas:
        print(data)
        if kitta in data[0]:
            dis = 10
            price = int(data[4])
            dic_price = price * (dis/100)
            total += price - dic_price
        else:
            print("not found ")
    print(total)

calculate_discount(kitta_no)