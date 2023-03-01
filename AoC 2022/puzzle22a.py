import collections
import copy

file = open("puzzle22.txt", "r")
read = file.readlines()


class Hero:
    def __init__(self, pos, face) -> None:
        self.position = pos
        self.facing = face

    def getFace(self):
        return self.facing[0]

    def getPos(self):
        return self.position

    def turn(self, letter):
        if letter == "R":
            faces = self.facing
            faces.rotate(-1)
        if letter == "L":
            faces = self.facing
            faces.rotate(1)

    def Move(self, integer_val, board):
        steps = 0
        while steps < integer_val:
            current = self.getPos()
            next = self.getFace()
            # print("checkboard:")
            # print(checkBoard(current,next,board))
            match checkBoard(current, next, board):
                case -1:
                    # print("case -1 of checkboard")
                    # we will hit a zero, get warped
                    posi = warp(current, next, board)
                    self.position = posi
                case 0:
                    # print("case 0 of checkboard")
                    # either we will hit a tree or we will warp and hit a tree
                    self.position = current
                    break
                case 1:
                    # print("case 1 of checkboard")
                    # everythings good, keep going
                    resultant = tupAdd(current, next)
                    self.position = resultant
            steps += 1
            # print(self.getPos())


def checkBoard(current, next, board):
    resultant = tupAdd(current, next)
    x = resultant[0]
    y = resultant[1]
    # print("resultant")
    # print(resultant)
    # print("line 50")
    # print(board[y][x])
    if board[y][x] == ".":
        return 1
    if board[y][x] == "#":
        return 0
    if board[y][x] == 0:
        warped_pos = warp(resultant, next, board)
        # print("line63")
        # print(warped_pos)
        j = warped_pos[0]
        i = warped_pos[1]
        if board[i][j] == "#":
            return 0
        elif board[i][j] == ".":
            return -1


def warp(pos, next, board):
    x = pos[0]
    y = pos[1]
    # print("warped!!")
    # print(pos)
    match next:
        case (1, 0):
            for j in range(len(board[y])):
                if board[y][j] != 0:
                    return (j, y)
        case (0, 1):
            for i in range(len(board)):
                if board[i][x] != 0:
                    return (x, i)
        case (-1, 0):
            for j in range(len(board[y]) - 1, -1, -1):
                # print(y,j)
                if board[y][j] != 0:
                    return (j, y)
        case (0, -1):
            for i in range(len(board) - 1, -1, -1):
                if board[i][x] != 0:
                    return (x, i)


def findTopLeft(board):
    pos = (-1, -1)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                pos = (j, i)
                return pos


def finPassword(position, offset, facing, board):
    row = position[1] - offset + 1
    column = position[0] - offset + 1
    match facing:
        case (1, 0):
            face = 0
        case (0, 1):
            face = 1
        case (-1, 0):
            face = 2
        case (0, -1):
            face = 3
    ans = (1000 * row) + (4 * column) + face
    return ans


def tupAdd(x, y):
    results = map(lambda val1, val2: val1 + val2, x, y)
    results = tuple(results)
    return results


def arrayPrint(array):
    length = len(array)
    for i in range(length):
        for j in range(len(array[i])):
            print(array[i][j], end="")
        print("\n", end="")


board = [[0 for i in range(0, 3000)] for j in range(0, 3000)]

offset = 2
# arrayz=[[0 for i in range(40)] for j in range(40)]
arrayz = board
for i in range(len(read)):
    if i == len(read) - 1:
        input = read[i].strip()
        break
    input = read[i].replace(" ", "0")
    for j in range(len(read[i])):
        if read[i][j] == "." or read[i][j] == "#":
            arrayz[i + offset][j + offset] = read[i][j]

# arrayPrint(arrayz)
# print(" ")
input = input.replace("R", ":R:")
input = input.replace("L", ":L:")
input = input.split(":")
# print(input)


facing = collections.deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
# print(facing)


pos = findTopLeft(arrayz)
hero = Hero(pos, facing)
# print(hero.getPos())
while input != []:
    copiez = copy.deepcopy(arrayz)
    # curr=hero.getPos()
    # match hero.getFace():
    # case (1,0):
    # sym='>'
    # case (0,1):
    # sym='v'
    # case (-1,0):
    # sym='<'
    # case (0,-1):
    # sym='^'
    # copiez[curr[1]][curr[0]]=sym
    # print(" ")
    # arrayPrint(copiez)
    # print(" ")
    next = input.pop(0)
    if next.isdigit() == True:
        # print("WALKING")
        # print(next)
        # print(hero.getFace())
        hero.Move(int(next), arrayz)
    else:
        # print("TURNING")
        hero.turn(next)
        # print(hero.getFace())
    # print(hero.getPos())

position = hero.getPos()
curr_facing = hero.getFace()
password = finPassword(position, offset, curr_facing, arrayz)
print("position,offset,curr_facing")
print(position, offset, curr_facing)
print("password")
print(password)
