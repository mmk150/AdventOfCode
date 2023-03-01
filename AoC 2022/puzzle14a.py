file = open("puzzle14.txt", "r")
read = file.readlines()


class Grain:
    def __init__(self):
        self.stopped = False
        self.abyss = False
        self.x = 500
        self.y = 0
        self.steps = 0

    def abyssCheck(self):
        if self.steps > 1000:
            self.abyss = True
            self.stopped = True
        return self.abyss

    def stopCheck(self, arr):
        xval = self.x
        yval = self.y
        # print(yval)
        # print(xval)
        next_letter_down = arr[yval + 1][xval]
        diag_right = arr[yval + 1][xval + 1]
        diag_left = arr[yval + 1][xval - 1]
        if next_letter_down == ".":
            return (0, 1)
        if diag_left == ".":
            return (-1, 1)
        if diag_right == ".":
            return (1, 1)
        else:
            self.stopped = True
            return (0, 0)

    def update(self, arr):
        abyss = self.abyssCheck()
        if abyss:
            return
        vec = self.stopCheck(arr)
        if vec == (0, 0):
            i = self.y
            j = self.x
            arr[i][j] = "o"
        else:
            self.x = self.x + vec[0]
            self.y = self.y + vec[1]
            self.steps += 1

    def getPos(self):
        pos = (self.x, self.y)
        return pos

    def getStopped(self):
        return self.stopped


def arrayPrint(array):
    length = len(array)
    for i in range(length):
        for j in range(len(array[i])):
            print(array[i][j], end="")
        print("\n", end="")


def arrayCountStone(array):
    length = len(array)
    sum = 0
    for i in range(length):
        for j in range(len(array[i])):
            if array[i][j] == "#":
                sum = sum + 1
    return sum


def arrayCountSand(array):
    length = len(array)
    sum = 0
    for i in range(length):
        for j in range(len(array[i])):
            if array[i][j] == "o":
                sum = sum + 1
    return sum


def init(x_max, y_max):
    main_arr = []
    for i in range(y_max):
        arr = []
        for j in range(x_max):
            arr.append(".")
        main_arr.append(arr)
    return main_arr


def signed(x_1, x_2):
    if x_1 > x_2:
        return -1
    if x_1 < x_2:
        return 1


def draw(arr, pos1, pos2):
    i = pos1[1]
    j = pos1[0]
    endi = pos2[1]
    endj = pos2[0]
    # print(pos1)
    # print(pos2)
    # print("64")
    # print((j,i))
    # print((endj,endi))
    if i == endi:
        k = j
        sgn = signed(j, endj)
        while k != endj:
            arr[i][k] = "#"
            # print((i, k))
            k += sgn
        arr[i][k] = "#"
        # print((i,k))
    else:
        k = i
        sgn = signed(i, endi)
        while k != endi:
            arr[k][j] = "#"
            # print((k, j))
            k += sgn
        arr[k][j] = "#"
        # print((k,j))


cave_arr = init(2000, 2000)
max_y = 0
for line in read:
    ordered_pairs = []
    splitline = line.strip().split("->")
    for pairs in splitline:
        pairs = pairs.strip().split(",")
        pos = (int(pairs[0]), int(pairs[1]))
        if pos[1] > max_y:
            max_y = pos[1]
        ordered_pairs.append(pos)
    for i in range(len(ordered_pairs) - 1):
        pos1 = ordered_pairs[i]
        pos2 = ordered_pairs[i + 1]
        draw(cave_arr, pos1, pos2)

print(arrayCountStone(cave_arr))

cave_arr[0][500] = "+"

current = Grain()
grains = []
while not current.abyssCheck():
    current = Grain()
    grains.append(current)
    while not current.getStopped():
        current.update(cave_arr)
    # print(current.getPos())
print(len(grains) - 1)
