file = open("puzzle3.txt", "r")
read = file.readlines()

string = "abcdefghijklmnopqrstuvwxyz"
string = string + string.upper()

priorities = list(string)
decode = lambda char: priorities.index(char) + 1
priority_sum = 0

for line in read:
    line = line.strip()
    # strip whitespace
    length = len(line)
    half = int(length / 2)
    # get half the length
    left = set(line[0:half])
    right = set(line[half:])
    # get the left half and the right half, turn into sets
    ans = left.intersection(right)

    for x in ans:
        priority_sum += decode(x)

print(priority_sum)
