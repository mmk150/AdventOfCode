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


file = open("puzzle13.txt", "r")
read = file.readlines()
input_arr = []
for i in range(len(read)):
    read[i] = read[i].strip()
    if len(read[i]) != 0:
        input_arr.append(read[i])

length = len(input_arr)
hlength = length / 2

pairs = []
for i in range(0, length, 2):
    line_1 = eval(input_arr[i])
    line_2 = eval(input_arr[i + 1])
    z = listComp(line_1, line_2)
    # print(line_1)
    # print(line_2)
    if z == 1:
        pairs.append((i // 2) + 1)
x = sum(pairs)
print(x)
