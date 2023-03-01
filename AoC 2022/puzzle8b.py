import copy
import math

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
                temp[i][j] = 0
            if j == 0 or j == width - 1:
                temp[i][j] = 0
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


def findScenicScore(array, i, j):
    lv = 0
    rv = 0
    tv = 0
    bv = 0
    length = len(array)
    height = array[i][j]
    width = len(array[0])
    for k in range(j - 1, -1, -1):
        if array[i][k] < height:
            lv += 1
        if array[i][k] >= height:
            lv += 1
            break
    for k in range(j + 1, width):
        if array[i][k] < height:
            rv += 1
        if array[i][k] >= height:
            rv += 1
            break
    for k in range(i - 1, -1, -1):
        if array[k][j] < height:
            tv += 1
        if array[k][j] >= height:
            tv += 1
            break
    for k in range(i + 1, length):
        if array[k][j] < height:
            bv += 1
        if array[k][j] >= height:
            bv += 1
            break
    return lv * rv * bv * tv


def countMax(array):
    length = len(array)
    biggest = 0
    for i in range(length):
        for j in range(len(array[i])):
            if array[i][j] > biggest:
                biggest = array[i][j]
    return biggest


copy_array = copy.deepcopy(read)
copy_array = perimeterFill(copy_array)


length = len(read)
width = len(read)

for i in range(length):
    for j in range(width):
        if copy_array[i][j] == 0:
            continue
        else:
            copy_array[i][j] = findScenicScore(read, i, j)


ans = countMax(copy_array)
print(ans)
