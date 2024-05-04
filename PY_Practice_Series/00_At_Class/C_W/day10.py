# # open file
# file = open("lab7.txt")
# # raed file
# contents = file.read()
# file.close()
# # after reding split iit into list by space paramater
# data = contents.split("\n")
# # print(data)
# # append further splited data
# listData = []
# for row in data:
#     cledRow =  row.split("\n")
#     listData.append(cledRow)
# print(listData)




def data_into_list(filename="lab7.txt"):
    with open(filename, 'r') as file:
        contents = file.read()

    data = contents.split("\n")
    result = []

    for line in data:
        if line == "":
            continue
        values = line.split(", ")
        entry = {
            "id": values[0],
            "location": values[1],
            "direction": values[2],
            "anna": values[3],
            "price": values[4],
            "availability": values[5].strip()
        }
        result.append(entry)

    return result


def save_data_to_file(data, filename="lab7.txt"):
    with open(filename, 'w') as file:
        for entry in data:
            modified_data = ", ".join(entry.values()) + "\n"
            file.write(modified_data)


def writeFile(path):
    # Process the original data
    original_data = data_into_list(path)

    # Loop through the data and modify where needed
    for data in original_data:
        if data["id"] == "102":
            data["availability"] = "Not Available"
            break

    # Print modified data
    for data in original_data:
        modified_data = ", ".join(data.values())
        print(modified_data)

    # Save the modified data to file
    save_data_to_file(original_data)

    return original_data


# Call the function to execute the code
data = writeFile("lab7.txt")