file = open("puzzle3.txt", "r")
read = file.readlines()

string = "abcdefghijklmnopqrstuvwxyz"
string = string + string.upper()

priorities = list(string)
decode = lambda char: priorities.index(char) + 1

priority_sum = 0
arr = []

for line in read:
    line = line.strip()
    arr.append(line)
    if len(arr) == 3:
        set1 = set(arr[0])
        set2 = set(arr[1])
        set3 = set(arr[2])
        ans = set1.intersection(set2.intersection(set3))
        for x in ans:
            priority_sum += decode(x)
        arr = []

print(priority_sum)
