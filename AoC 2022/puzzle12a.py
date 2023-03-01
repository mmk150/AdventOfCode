import bisect

file = open("puzzle12.txt", "r")
read = file.readlines()
for i in range(len(read)):
    read[i] = read[i].strip()


def edgedelta(char1, char2):
    if char1 == "S":
        char1 = "a"
    if char2 == "S":
        char2 == "a"
    if char1 == "E":
        char1 = "z"
    if char2 == "E":
        char2 = "z"
    alpha = "abcdefghijklmnopqrstuvwxyz"
    val1 = alpha.find(char1)
    val2 = alpha.find(char2)
    metric = val2 - val1
    if metric <= 1:
        metric = 1
    if metric > 2:
        metric = 99999
    return metric


def arrayPrint(array):
    length = len(array)
    for i in range(length):
        for j in range(len(array[i])):
            print(array[i][j], end="")
        print("\n", end="")


def arrayPrintPaths(path, length, width):
    for i in range(length):
        for j in range(width):
            val = path[(i, j)]
            if val == 9999999:
                print(".", end=",")
            else:
                print(path[(i, j)], end=",")
        print("\n", end="")


def get_adjacent(i, j, length, width):
    adj = []
    for dx, dy in ([0, 1], [1, 0], [-1, 0], [0, -1]):
        a, b = i + dy, j + dx
        if a >= 0 and b < width and b >= 0 and a < length:
            adj.append((a, b))
    return adj


def Dijkstras(graph, source, end):
    distances = dict()
    distances.update({source: 0})
    que = []
    visited = set()
    for k, v in graph.items():
        if k != source:
            distances.update({k: 9999999})
        q = (k[0], k[1], distances[k])
        que.append()
    first = True
    while True:
        if not que:
            break
        # print(que)
        # print(distances)
        # print(list)
        que.sort(key=lambda x: distances[x])
        # print(list)
        vert = que[0]
        que.remove(vert)
        if vert not in visited:
            visited.add(vert)
            for neighbor in graph[vert]:
                if neighbor[0] in que:
                    new_dist = distances[vert] + neighbor[1]

                    if new_dist < distances[neighbor[0]]:
                        distances.pop(neighbor[0])
                        distances.update({neighbor[0]: new_dist})
                que.remove(neighbor[0])
                bisect.insert(neighbor[0])
    return distances


def graphBuilder(array):
    length = len(array)
    width = len(array[0])
    graph = dict()
    for i in range(length):
        for j in range(width):
            letter = array[i][j]
            if letter == "S":
                start = (i, j)
            if letter == "E":
                end = (i, j)
            adj = get_adjacent(i, j, length, width)
            actual_neighbors = []
            for letters in adj:
                x, y = letters[0], letters[1]
                letter2 = array[x][y]
                dist = edgedelta(letter, letter2)
                if dist <= 1:
                    actual_neighbors.append([letters, dist])
                graph.update({(i, j): actual_neighbors})
    return graph, start, end


# arrayPrint(read)
graph, start, end = graphBuilder(read)
# print(start)
# print(end)
length = len(read)
width = len(read[0])

paths = Dijkstras(graph, start, end)

# print(paths[(20,3)])
# print(graph[(20,3)])
# print(graph[(20,2)])
# print(graph[(20,1)])
# print(graph[(20,0)])
print(paths[end])
