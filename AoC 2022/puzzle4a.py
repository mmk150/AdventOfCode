file = open("puzzle4.txt", "r")
read = file.readlines()


def nestedCheck(arr1, arr2):
    # Checks if the interval [a,b] is contained in [x,y] or vice versa
    a = arr1[0]
    b = arr1[1]
    x = arr2[0]
    y = arr2[1]
    if a <= x:
        if b >= y:
            return 1
    if x <= a:
        if y >= b:
            return 1
    return 0


def Elf2Mathematician(stringy):
    hyphen_index = stringy.find("-")
    a = stringy[0:hyphen_index]
    b = stringy[hyphen_index + 1 :]
    return [int(a), int(b)]


nested_count = 0

for line in read:
    line = line.strip()
    comma_index = line.find(",")
    first = line[0:comma_index]
    first = Elf2Mathematician(first)
    # Gets the first pair, turns it into an array with two entries
    second = line[comma_index + 1 :]
    second = Elf2Mathematician(second)
    # Gets the first pair, turns it into an array with two entries
    nested_count += nestedCheck(first, second)

print(nested_count)
