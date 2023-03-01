import copy
import math
from collections import defaultdict, deque


class Node:
    def __init__(self, pos):
        self.pos = pos
        self.f_val = 0
        self.g_val = 0
        self.h_val = 0
        self.parent = None
        self.children = None

    def setFGH(self, f_new, g_new, h_new):
        self.f_val = f_new
        self.g_val = g_new
        self.h_val = h_new

    def getFGH(self):
        return (self.f_val, self.g_val, self.h_val)

    def getPos(self):
        return self.pos

    def setParent(self, new_parent):
        self.parent = new_parent

    def getParent(self):
        return self.parent


file = open("puzzle24.txt", "r")
read = file.readlines()
for i in range(len(read)):
    read[i] = read[i].strip()


board = [[0 for x in range(len(read[0]))] for x in range(len(read))]

for i in range(len(read)):
    for j in range(len(read[i])):
        board[i][j] = read[i][j]


def arrayPrint(array):
    length = len(array)
    for i in range(length):
        for j in range(len(array[i])):
            print(array[i][j], end="")
        print("\n", end="")


arrayPrint(board)


def build3Graph(board):
    t = 0
    width = len(board[0])
    height = len(board)
    emptyw = width - 2
    emptyh = height - 2
    prod = math.lcm(emptyw, emptyh)

    def default_val():
        return True

    graph = defaultdict(default_val)
    t = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            sym = board[i][j]
            pos = (j, i, t)
            if sym != ".":
                graph.update({pos: False})
                x = pos[0]
                y = pos[1]
                match sym:
                    case ">":
                        for time in range(0, 3 * prod):
                            x_new = ((x - 1) + time) % emptyw + 1
                            new_pos = (x_new, y, time)
                            graph.update({new_pos: False})
                    case "<":
                        for time in range(0, 3 * prod):
                            x_new = ((x - 1) - time) % emptyw + 1
                            new_pos = (x_new, y, time)
                            graph.update({new_pos: False})
                    case "^":
                        for time in range(0, 3 * prod):
                            y_new = ((y - 1) - time) % emptyh + 1
                            new_pos = (x, y_new, time)
                            graph.update({new_pos: False})
                    case "v":
                        for time in range(0, 3 * prod):
                            y_new = ((y - 1) + time) % emptyh + 1
                            new_pos = (x, y_new, time)
                            graph.update({new_pos: False})
            if sym == "#":
                for time in range(0, 3 * prod):
                    newpos = (j, i, time)
                    graph.update({newpos: False})

    return graph, prod


def isEnd(current, end):
    # current=current.getPos()
    if current[0] == end[0] and current[1] == end[1]:
        return True
    else:
        return False


def eucDistance(pos1, pos2):
    dist = abs(pos1[1] - pos2[1]) + abs(pos1[0] - pos2[0])
    return dist


def fghcalc(path, target, end):
    f = 0
    g = len(path) + 1
    h = eucDistance(target, end)
    f = g + h
    return f, g, h


def getNext(nlist, scores_dict):
    newlist = [(scores_dict[x], x) for x in nlist]
    newlist.sort(key=lambda e: e[0])
    last = newlist[0][1]
    return last


def getChildren(pos, end):
    # pos=pos.getPos()
    x = pos[0]
    y = pos[1]
    end_x = end[0]
    end_y = end[1]
    t = pos[2]
    new_t = t + 1
    children = []
    if x == 1 and y == 0:
        return [(1, 0, new_t), (1, 1, new_t)]

    if x == 1 and y == 1:
        return [(1, 0, new_t), (1, 2, new_t), (2, 1, new_t), (1, 1, new_t)]

    else:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if x + j >= 1 and y + i >= 1 and x + j <= end_x and y + i < end_y:
                    new_pos1 = (x + j, y, new_t)
                    new_pos2 = (x, y + i, new_t)
                    if new_pos1 not in children:
                        children.append(new_pos1)
                    if new_pos2 not in children:
                        children.append(new_pos2)

    if x == end_x and y == end_y - 1:
        return [(x, y, new_t), (x - 1, y, new_t), (x, y - 1, new_t), (x, y + 1, new_t)]

    if x == end_x and y == end_y:
        return [(x, y, new_t), (x, y - 1, new_t)]
    return children


def BFS(graph, start, end):
    unvisited = deque()

    def def_val():
        return False

    visited = defaultdict(def_val)

    unvisited.append(start)
    count = 0
    while unvisited != [] and count < 2000000:
        current = unvisited.popleft()
        # if count% 100==0:
        # print("current is")
        # print(current)
        # print('count is:')
        # print(count)
        visited[current] = True
        if isEnd(current, end):
            # print("We hit the end!")
            return current
        else:
            child_list = getChildren(current, end)
            # print(len(child_list))
            for child in child_list:
                # print("Child is:")
                # print(child)
                if visited[child] == True or graph[child] == False:
                    continue
                else:
                    unvisited.append(child)
                    visited.update({child: True})
        count += 1
    return False


i = len(board) - 1
endx = 0
endy = i
for j in range(len(board[i]) - 1):
    if board[i][j] == "#" and board[i][j + 1] == ".":
        endx = j + 1
        break
end = (endx, endy)

graphSample, period = build3Graph(board)

print(len(graphSample))
print(period)
start = (1, 0, 0)
last_node = BFS(graphSample, start, end)
print(last_node)
print("   ")


for t in range(0, 10):
    b = copy.deepcopy(board)
    for i in range(len(b)):
        for j in range(len(b[i])):
            if graphSample[(j, i, t)] == False:
                b[i][j] = "B"
            else:
                b[i][j] = "."
    arrayPrint(b)
    print("   ")
