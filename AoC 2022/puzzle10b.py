file = open("puzzle10.txt", "r")
read = file.readlines()


class CycleTimer:
    def __init__(self, length, value_to_add):
        self.length = length
        self.value_to_add = value_to_add

    def decrementTimer(self):
        self.length += -1

    def getTimer(self):
        return self.length

    def getValue(self):
        return self.value_to_add


def updateq(arr):
    sum = 0
    for i in range(len(arr)):
        arr[i][1] += -1
        if arr[i][1] == 0:
            sum = sum + arr[i][2]
    return arr, sum


def getSig(arr, N):
    added = [entry[1] for entry in arr if entry[0] <= N]
    X = 1
    for number in added:
        X = X + number
    return [X, X * N]


height = 6
width = 40

screen = [["."] * width for i in range(height)]
print(screen)

X = 1
cycle = 1
command_queue = []
next_line = 0
end = len(read)
data = []

# x-> quotient,remainder  which is the row and column respectively


def cycle2array(cycle):
    temp = cycle
    temp = temp - 1
    row = temp // 40
    column = temp % 40
    return (row, column)


def drawScreen(pos, X, screen):
    drew = False
    row = pos[0]
    column = pos[1]
    possible = set([X, X - 1, X + 1])

    if column in possible:
        screen[row][column] = "#"
        drew = True
    return screen, drew, (row, column)


while next_line < end:
    if command_queue == []:
        x = read[next_line].split()
        if x[0] == "noop":
            command_queue.append(CycleTimer(1, 0))
        else:
            val = int(x[1])
            command_queue.append(CycleTimer(2, val))
        next_line += 1

    data.append([cycle, X])
    pos = cycle2array(cycle)
    # print(pos)
    # print(X)
    screen, drew, target = drawScreen(pos, X, screen)
    # if(drew):
    # print("I drew!")
    # print(target)
    # print("I drew!!")

    sum = 0

    coppy = []
    for comms in command_queue:
        comms.decrementTimer()
        if comms.getTimer() <= 0:
            sum = sum + comms.getValue()
        else:
            coppy.append(comms)
    command_queue = coppy

    X = X + sum
    cycle += 1


def arrayPrint(array):
    length = len(array)
    for i in range(length):
        for j in range(len(array[i])):
            print(array[i][j], end="")
        print("\n", end="")


arrayPrint(screen)
