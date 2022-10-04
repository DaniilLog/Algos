def build_tree_from_input(array):
    for i in range(len(array)):
        if array[i][1]:
            array[array[i][1] - 1] += [i, None]
        if array[i][2]:
            array[array[i][2] - 1] += [i, None]
    array[0] += [None, None]
    return array


def count_height(array, i):
    height = 1
    while i:
        if (not array[i][4]) or (array[i][4] and array[i][4] < height):
            array[i][4] = height
            height += 1
            i = array[i][3]
        else:
            break

    return array


def balance_tree(array):
    for i in range(len(array)):
        if not array[i][1] and not array[i][2]:
            array = count_height(array, i)
    for i in array:
        left = 0
        right = 0
        if i[1]:
            left = array[i[1] - 1][4]
        if i[2]:
            right = array[i[2] - 1][4]
        output.write(str(right - left) + "\n")


file = open("input.txt", "r")
output = open("output.txt", "w")
data = file.readlines()
data = data[1:]
input_data = []
for i in data:
    input_data.append(list(map(int, i.split())))
balance_tree(build_tree_from_input(input_data))
file.close()
output.close()
