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


X = 1
cycle = 1
command_queue = []
next_line = 0
end = len(read)
data = []

timer = CycleTimer(1, 0)
print(timer.getTimer())

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


desired = [20, 60, 100, 140, 180, 220]
desired = [x - 1 for x in desired]

signals = [a * b for [a, b] in data]
ref = [signals[i] for i in desired]

sum = 0
for x in ref:
    sum = sum + x
print(sum)
