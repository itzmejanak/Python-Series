# qn 2

matrix_a = [[1, 1, 5], [2, 4, 6], [3, 7, 8]]
matrix_b = [[7, 9, 0], [8, 8, 9], [7, 6, 9]]

def sum_matrices():
    sum_matrix = [[], [], []]
    counter = 0
    for row in matrix_a:
        counter_j = 0
        for each in row:
            sum_matrix[counter].append((each + matrix_b[counter][counter_j]) + 5)
            counter_j += 1
        counter += 1
    return sum_matrix

print(sum_matrices())


# qn 3
def search():
    choice_for_search = int(input("Enter your number: "))
    define_list = [2,9,9,9,78,90,3]
    found = 0
    count = 0
    for item in define_list:
        if (item == choice_for_search):
            found = item
    for newitem in define_list:
        if found == newitem:
            count += 1
    return count
print(search())    