import collections
import copy


class CubeFace:
    def __init__(self, number, land, neighbors=[]):
        self.land = land
        self.neighbors = neighbors
        self.name = number

    def getName(self):
        return self.name

    def getLand(self):
        return self.land

    def getNeighbors(self):
        return self.neighbors

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    def facing2Neighbor(self, facing):
        neighbors = self.getNeighbors()
        match facing:
            case (1, 0):
                return neighbors[0]
            case (0, 1):
                return neighbors[1]
            case (-1, 0):
                return neighbors[2]
            case (0, -1):
                return neighbors[3]


class Hero:
    def __init__(self, pos, face, transitions) -> None:
        self.position = pos
        self.cubelandpos = pos
        self.facing = face
        self.cube_face = 0
        self.transitions = transitions

    def getTrans(self):
        return self.transitions

    def setCube(self, cube_face):
        self.cube_face = cube_face

    def setCubeLand(self, pos):
        self.cubelandpos = pos

    def getCubeLand(self):
        return self.cubelandpos

    def getCube(self):
        return self.cube_face

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

    def Move(self, integer_val):
        steps = 0
        while steps < integer_val:
            current_cube_pos = self.getCubeLand()
            current_cube = self.getCube()
            cube_board = current_cube.getLand()
            next = self.getFace()
            match checkBoard(self, current_cube_pos, next, cube_board):
                case -1:
                    # Must warp
                    # print("warped!")
                    posi, neighbor, spin = self.warp(current_cube, next, cube_board)
                    self.cubelandpos = posi
                    self.setCube(neighbor)
                    x = self.facing
                    x.rotate(spin)
                case 0:
                    # hit wall
                    # print("Hit wall")
                    break
                case 1:
                    # walk
                    # print("walk")
                    resultant = tupAdd(current_cube_pos, next)
                    self.cubelandpos = resultant
            steps += 1

    def warp(self, cube_face, next, cube_board):
        transitions = self.getTrans()
        num_cube = cube_face.getName()
        neighbor_cube = cube_face.facing2Neighbor(next)
        num_dest = neighbor_cube.getName()
        # print((num_cube,num_dest))
        funcs = transitions[(num_cube, num_dest)]
        new_position, spin = funcs(self.getCubeLand())
        # print(new_position,spin)

        return new_position, neighbor_cube, spin


def checkBoard(hero, current, next, board):
    resultant = tupAdd(current, next)
    x = resultant[0]
    y = resultant[1]
    if board[y][x] == ".":
        return 1
    if board[y][x] == "#":
        return 0
    if board[y][x] == 0:
        warped_pos, dest_cube, spin = hero.warp(hero.getCube(), next, board)
        j = warped_pos[0]
        i = warped_pos[1]
        new_board = dest_cube.getLand()
        if new_board[i][j] == "#":
            # print("Warp would hit wall")
            return 0
        elif board[i][j] == ".":
            # print("warp and walk")
            return -1


def findTopLeft(board):
    pos = (-1, -1)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                pos = (j, i)
                return pos


def finalPassword(cube, position, offset, facing):
    y = position[1]
    x = position[0]
    match cube:
        case 1:
            x += 50
        case 2:
            x += 100
        case 3:
            x += 50
            y += 50
        case 4:
            y += 100
        case 5:
            x += 50
            y += 100
        case 6:
            y += 150

    match facing:
        case (1, 0):
            face = 0
        case (0, 1):
            face = 1
        case (-1, 0):
            face = 2
        case (0, -1):
            face = 3
    print(y)
    print(x)
    print(face)
    ans = (1000 * y) + (4 * x) + face
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


file = open("puzzle22.txt", "r")
read = file.readlines()

subarr1 = []
subarr2 = []
subarr3 = []
subarr4 = []
subarr5 = []
subarr6 = []
for i in range(len(read)):
    if i == 50:
        break
    subarr1.append(read[i].strip()[0:50])
    subarr2.append(read[i].strip()[50:])

for i in range(50, 100):
    subarr3.append(read[i].strip()[0:50])

for i in range(100, 150):
    subarr4.append(read[i].strip()[0:50])
    subarr5.append(read[i].strip()[50:])

for i in range(150, 200):
    subarr6.append(read[i].strip())

# arrayPrint(subarr1)
# print(" ")
# arrayPrint(subarr2)
# print(" ")
# arrayPrint(subarr3)
# print(" ")
# arrayPrint(subarr4)
# print(" ")
# arrayPrint(subarr5)
# print(" ")
# arrayPrint(subarr6)


def prepSubArrs(subarr, offset):
    zeroes = [
        [0 for i in range(0 - offset, 50 + offset)]
        for j in range(0 - offset, 50 + offset)
    ]
    for i in range(len(subarr)):
        for j in range(len(subarr[i])):
            zeroes[i + offset][j + offset] = subarr[i][j]
    return zeroes


offset = 1

prepped_arr1 = prepSubArrs(subarr1, 1)
prepped_arr2 = prepSubArrs(subarr2, 1)
prepped_arr3 = prepSubArrs(subarr3, 1)
prepped_arr4 = prepSubArrs(subarr4, 1)
prepped_arr5 = prepSubArrs(subarr5, 1)
prepped_arr6 = prepSubArrs(subarr6, 1)

# print("total height")
# print(len(prepped_arr1))
# print("total width")
# print(len(prepped_arr1[0]))


cubeFace1 = CubeFace(1, prepped_arr1)
cubeFace2 = CubeFace(2, prepped_arr2)
cubeFace3 = CubeFace(3, prepped_arr3)
cubeFace4 = CubeFace(4, prepped_arr4)
cubeFace5 = CubeFace(5, prepped_arr5)
cubeFace6 = CubeFace(6, prepped_arr6)

cubeFace1.setNeighbors([cubeFace2, cubeFace3, cubeFace4, cubeFace6])
cubeFace2.setNeighbors([cubeFace5, cubeFace3, cubeFace1, cubeFace6])
cubeFace3.setNeighbors([cubeFace2, cubeFace5, cubeFace4, cubeFace1])
cubeFace4.setNeighbors([cubeFace5, cubeFace6, cubeFace1, cubeFace3])
cubeFace5.setNeighbors([cubeFace2, cubeFace6, cubeFace4, cubeFace3])
cubeFace6.setNeighbors([cubeFace5, cubeFace2, cubeFace1, cubeFace4])

transitions = dict()

transitions.update({(1, 2): lambda pos: ((0 + offset, pos[1]), 0)})
transitions.update({(1, 3): lambda pos: ((pos[0], 0 + offset), 0)})
transitions.update({(1, 4): lambda pos: ((0 + offset, 50 - pos[1] + offset), -2)})
transitions.update({(1, 6): lambda pos: ((0 + offset, pos[0]), -1)})

transitions.update({(2, 5): lambda pos: ((49 + offset, 50 - pos[1] + offset), 2)})
transitions.update({(2, 3): lambda pos: ((49 + offset, pos[0]), -1)})
transitions.update({(2, 1): lambda pos: ((49 + offset, pos[1]), 0)})
transitions.update({(2, 6): lambda pos: ((pos[0], 49 + offset), 0)})

transitions.update({(3, 2): lambda pos: ((pos[1], 49 + offset), 1)})
transitions.update({(3, 5): lambda pos: ((pos[0], 0 + offset), 0)})
transitions.update({(3, 4): lambda pos: ((pos[1], 0 + offset), 1)})
transitions.update({(3, 1): lambda pos: ((pos[0], 49 + offset), 0)})

transitions.update({(4, 5): lambda pos: ((0 + offset, pos[1]), 0)})
transitions.update({(4, 6): lambda pos: ((pos[0], 0 + offset), 0)})
transitions.update({(4, 1): lambda pos: ((0 + offset, 50 - pos[1] + offset), 2)})
transitions.update({(4, 3): lambda pos: ((0 + offset, pos[0]), -1)})

transitions.update({(5, 2): lambda pos: ((49 + offset, 50 - pos[1] + offset), 2)})
transitions.update({(5, 6): lambda pos: ((49 + offset, pos[0]), -1)})
transitions.update({(5, 4): lambda pos: ((49 + offset, pos[1]), 0)})
transitions.update({(5, 3): lambda pos: ((pos[0], 49 + offset), 0)})


transitions.update({(6, 5): lambda pos: ((pos[1], 49 + offset), 1)})
transitions.update({(6, 2): lambda pos: ((pos[0], 0 + offset), 0)})
transitions.update({(6, 1): lambda pos: ((pos[1], 0 + offset), 1)})
transitions.update({(6, 4): lambda pos: ((pos[0], 49 + offset), 0)})

board = [[0 for i in range(0, 3000)] for j in range(0, 3000)]

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
#print(" ")
input = input.replace("R", ":R:")
input = input.replace("L", ":L:")
input = input.split(":")
#print(input)

# input=['R','1','1','L']
# input.extend(['1' for x in range(200)])


facing = collections.deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
#print(facing)


pos = findTopLeft(arrayz)
hero = Hero(pos, facing, transitions)
hero.setCube(cubeFace1)
hero.setCubeLand((1, 1))
#print(hero.getPos())


count = 0
positions = []
while input != []:
    positions.append((hero.getCube(), hero.getCubeLand(), hero.getFace()))
    next = input.pop(0)
    #print("Current pos:", end="")
    #print(hero.getCubeLand(), end=" . ")
    #print("Next is: ", end="")
    #print(next, end="")
    #print(hero.getFace(), end="\n")
    if next.isdigit() == True:
        hero.Move(int(next))
    else:
        hero.turn(next)
    #print("Current cube face:", end="")
    #print(hero.getCube().getName(), end="\n")
    #print("Cubeland pos:", end="")
    #print(hero.getCubeLand())
    count += 1

cube = hero.getCube().getName()
cube_land_pos = hero.getCubeLand()
curr_facing = hero.getFace()

print("cube,cubelandpos,curr_facing")
print(cube, cube_land_pos, curr_facing)


password = finalPassword(cube, cube_land_pos, offset, curr_facing)
print("position,offset,curr_facing")
print(cube, cube_land_pos, offset, curr_facing)
print("password")
print(password)
