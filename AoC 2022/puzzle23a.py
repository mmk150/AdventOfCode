import copy
import collections


class Elf:
    def __init__(self, location, moves, jolly=False):
        self.location = location
        self.jolly = jolly
        self.moves = moves

    def isJolly(self):
        self.jolly = True

    def isNotJolly(self):
        self.jolly = False

    def getJolly(self):
        return self.jolly

    def getLoc(self):
        return self.location

    def getMoves(self):
        return self.moves

    def firstHalf(self, board):
        coord = self.getLoc()
        move_list = self.getMoves()
        final_move = -1
        for move in move_list:
            # print(move,end=",")
            if checkMove(coord, move, board):
                final_move = move
                break
        # print(" ")
        # print(final_move)
        delta = moveConv(final_move)
        # print(delta)
        # print(coord)
        new_coord = tupAdd(coord, delta)
        # print(new_coord)
        return new_coord

    def secondHalf(self, coord, board):
        x = coord[0]
        y = coord[1]
        current = self.getLoc()
        a = current[0]
        b = current[1]
        board[b][a] = "."
        board[y][x] = "#"
        self.location = coord

    def finish(self, board):
        coord = self.getLoc()
        x = coord[0]
        y = coord[1]
        board[y][x] = "#"
        self.location = coord


def tupAdd(x, y):
    results = map(lambda val1, val2: val1 + val2, x, y)
    results = tuple(results)
    return results


def checkMove(coord, move, board):
    x = coord[0]
    y = coord[1]
    valid = True
    if move == 0:
        # North
        for i in [-1, 0, 1]:
            if board[y - 1][x + i] != ".":
                valid = False
    if move == 1:
        # South
        for i in [-1, 0, 1]:
            if board[y + 1][x + i] != ".":
                valid = False
    if move == 2:
        # West
        for i in [-1, 0, 1]:
            if board[y + i][x - 1] != ".":
                valid = False
    if move == 3:
        # East
        for i in [-1, 0, 1]:
            if board[y + i][x + 1] != ".":
                valid = False
    return valid


def moveConv(move):
    if move == 0:
        # North
        return (0, -1)
    if move == 1:
        # South
        return (0, 1)
    if move == 2:
        # West
        return (-1, 0)
    if move == 3:
        # East
        return (1, 0)
    else:
        return (0, 0)


def checkPos(coord, board):
    x = coord[0]
    y = coord[1]
    alone = True
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                sym = board[y + i][x + j]
                if sym != ".":
                    alone = False
    return alone


def checkJolly(elves_list, board):
    jolly = []
    unhappy = []
    for elf in elves_list:
        coord = elf.getLoc()
        if checkPos(coord, board):
            elf.isJolly()
            jolly.append(elf)
        else:
            elf.isNotJolly()
            unhappy.append(elf)
    return jolly, unhappy


def arrayPrint(array):
    length = len(array)
    for i in range(length):
        for j in range(len(array[i])):
            print(array[i][j], end="")
        print("\n", end="")


moves = [0, 1, 2, 3]
moves = collections.deque(moves)
# print("start")
# print(moves)
# print("one move")
moves.rotate(-1)
# print(moves)
# print("two move")
moves.rotate(-1)
# print(moves)
# print("three move")
moves.rotate(-1)
# print(moves)
# print("four move==start")
moves.rotate(-1)
# print(moves)


file = open("puzzle23.txt", "r")
read = file.readlines()

dim = len(read) + 200

center = dim // 2

elves = []
board = [["." for i in range(0, dim)] for j in range(0, dim)]
# zeroes=[[0 for i in range(0, dim)] for j in range(0, dim)]

# for line in read:
# print(line, end="")


for i in range(len(read)):
    for j in range(len(read[i])):
        if read[i][j] == "#":
            board[center + i][center + j] = "#"
            new_coord = (center + j, center + i)
            new_elf = Elf(new_coord, moves)
            elves.append(new_elf)


jolly, unhappy = checkJolly(elves, board)
count = 0

# arrayPrint(board)


while unhappy != [] and count < 1000:
    # print("count =", end="")
    # print(count)
    # print("len unhappy:")
    # print(len(unhappy))
    # print("len jolly")
    # print(len(jolly))
    # print("count:")
    # print(count)
    # blank=[[0 for i in range(0, dim)] for j in range(0, dim)]
    moves_dict = collections.defaultdict(list)
    for elf in unhappy:
        coord = elf.firstHalf(board)
        moves_dict[coord].append(elf)
    for key, values in moves_dict.items():
        # print(key)
        # print(values)
        if len(values) > 1:
            continue
        elf = values.pop()
        # print("Elf we're moving:")
        # print(elf.getLoc())
        # print("No more elf")
        coord = key
        elf.secondHalf(coord, board)
    # for elf in elves:
    # elf.finish(board)

    # print(elves[0].moves)
    moves.rotate(-1)
    jolly, unhappy = checkJolly(elves, board)
    count += 1
    # arrayPrint(board)


def rectBounds(elf_list, maxval):
    xmin = maxval
    xmax = 0
    ymin = maxval
    ymax = 0
    for elf in elf_list:
        coord = elf.getLoc()
        x = coord[0] + 1
        y = coord[1] + 1
        if x >= xmax:
            xmax = x
        if y >= ymax:
            ymax = y
        if x < xmin:
            xmin = x
        if y < ymin:
            ymin = y
    num_x_min = 0
    num_x_max = 0
    num_y_min = 0
    num_y_max = 0
    for elf in elf_list:
        coord = elf.getLoc()
        x = coord[0]
        y = coord[1]
        if x == xmax:
            num_x_max += 1
        if y > ymax:
            num_y_max += 1
        if x == xmin:
            num_x_min += 1
        if y < ymin:
            num_y_min += 1
    return ([xmin, xmax, ymin, ymax], [num_x_min, num_x_max, num_y_min, num_y_max])


print("No elves moved after round:")
print(count)
bounds = rectBounds(elves, len(board) * 2)
# print("xmin","xmax","ymin","ymax")
# print(bounds[0])
# print("numxmin","numxmax","numymin","numymax")
# print(bounds[1])
bounds = bounds[0]
width = bounds[1] - bounds[0] + 1
height = bounds[3] - bounds[2] + 1
# print("height","width","merp","product-number of elves")
# print(height,width, "merp", (height*width)-len(elves))
# print("elves,jolly,unhappy")
print(len(elves), len(jolly), len(unhappy))
