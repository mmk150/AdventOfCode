def listComp(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    i = 0
    j = 0
    results = 0
    while i < len1 and j < len2:
        list1_elem = list1[i]
        list2_elem = list2[j]
        # print(list1_elem,list2_elem)
        # print(" line 14")
        if isinstance(list1_elem, int):
            if isinstance(list2_elem, int):
                results = intComp(list1_elem, list2_elem)
            else:
                temp = [list1_elem]
                results = listComp(temp, list2_elem)
        if isinstance(list1_elem, list):
            if isinstance(list2_elem, int):
                temp = [list2_elem]
                results = listComp(list1_elem, temp)
            else:
                results = listComp(list1_elem, list2_elem)
        if results != 0:
            return results
        i += 1
        j += 1
    if j == len2 and i < len1:
        results = -1
    if i == len1 and j < len2:
        results = 1
    return results


def intComp(int1, int2):
    if int1 < int2:
        return 1
    if int1 == int2:
        return 0
    if int1 > int2:
        return -1


def isLessThan(x, y):
    ans = listComp(x, y)
    if ans == 1:
        return True
    if ans == -1:
        return False


def countMessagesLessThan(arr, x):
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            continue
        else:
            if isLessThan(arr[i], x):
                count += 1
    return count


file = open("puzzle13.txt", "r")
read = file.readlines()
input_arr = []
for i in range(len(read)):
    read[i] = read[i].strip()
    if len(read[i]) != 0:
        input_arr.append(eval(read[i]))

length = len(input_arr)
hlength = length / 2

divider1 = [[2]]
divider2 = [[6]]

num1 = countMessagesLessThan(input_arr, divider1) + 1
num2 = countMessagesLessThan(input_arr, divider2) + 2
prod = num1 * num2
print(prod)
