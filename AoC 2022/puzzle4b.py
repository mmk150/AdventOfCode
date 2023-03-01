file = open("puzzle4.txt", "r")
read = file.readlines()


def overlapCheck(arr1, arr2):
    # Checks if the intervals [a,b] and [x,y] have nonempty intersection
    a = arr1[0]
    b = arr1[1]
    x = arr2[0]
    y = arr2[1]
    if a <= y:
        if a >= x:
            return 1
    if b >= x:
        if b <= y:
            return 1
    if x <= b:
        if x >= a:
            return 1
    return 0


def Elf2Mathematician(stringy):
    hyphen_index = stringy.find("-")
    a = stringy[0:hyphen_index]
    b = stringy[hyphen_index + 1 :]
    return [int(a), int(b)]


overlap_count = 0

for line in read:
    line = line.strip()
    comma_index = line.find(",")
    first = line[0:comma_index]
    first = Elf2Mathematician(first)
    # Gets the first pair, turns it into an array with two entries
    second = line[comma_index + 1 :]
    second = Elf2Mathematician(second)
    # Gets the first pair, turns it into an array with two entries
    overlap_count += overlapCheck(first, second)

print(overlap_count)
