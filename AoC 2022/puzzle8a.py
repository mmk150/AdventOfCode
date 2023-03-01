import copy

file = open("puzzle8.txt", "r")
read = file.readlines()
length = len(read)

for i in range(length):
    read[i] = read[i].replace("\n", "")
    arr = []
    for j in range(len(read[i])):
        arr.append(int(read[i][j]))
    read[i] = arr


def arrayPrint(array):
    length = len(array)
    for i in range(length):
        for j in range(len(array[i])):
            print(array[i][j], end="")
        print("\n", end="")


def zeroes(array):
    length = len(array)
    for i in range(length):
        for j in range(len(array[i])):
            array[i][j] = 0
    return array


def perimeterFill(array1):
    # copies array1's perimeter to array2
    length = len(array1)
    width = len(array1[0])
    temp = copy.deepcopy(array1)
    for i in range(length):
        for j in range(width):
            if i == 0 or i == length - 1:
                temp[i][j] = "V"
            if j == 0 or j == width - 1:
                temp[i][j] = "V"
    return temp


def findVisible(array, i, j):
    visible = 0
    lvis = True
    rvis = True
    topvis = True
    botvis = True
    length = len(array)
    height = array[i][j]
    width = len(array[0])
    for k in range(0, j):
        if array[i][k] >= height:
            lvis = False
    for k in range(j + 1, width):
        if array[i][k] >= height:
            rvis = False
    for k in range(0, i):
        if array[k][j] >= height:
            botvis = False
    for k in range(i + 1, length):
        if array[k][j] >= height:
            topvis = False
    if lvis or rvis or topvis or botvis:
        visible = 1
    if visible == 1:
        return "V"
    else:
        return "X"


def countVisible(array):
    length = len(array)
    sum = 0
    for i in range(length):
        for j in range(len(array[i])):
            if array[i][j] == "V":
                sum = sum + 1
    return sum


copy_array = copy.deepcopy(read)
copy_array = zeroes(copy_array)
copy_array = perimeterFill(copy_array)


length = len(read)
width = len(read)

for i in range(length):
    for j in range(width):
        if copy_array[i][j] == "V":
            continue
        else:
            copy_array[i][j] = findVisible(read, i, j)


ans = countVisible(copy_array)
print(ans)
