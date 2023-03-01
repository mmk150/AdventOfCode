file = open("puzzle18.txt", "r")
read = file.readlines()


class Cube:
    def __init__(self, center):
        self.center = center
        self.x = center[0]
        self.y = center[1]
        self.z = center[2]
        self.neighbors = set()
        self.exposed = 6

    def addNeighbor(self, neighbor):
        N = self.neighbors
        N.add(neighbor)
        self.neighbors = N

    def getNeighbors(self):
        return len(self.neighbors)

    def updateSA(self):
        self.exposed = self.exposed - self.getNeighbors()

    def getSA(self):
        return self.exposed


def add3tuple(tup1, tup2):
    result = tuple(map(lambda x, y: x + y, tup1, tup2))
    return result


def checkNeighbor(coords, dictionary):
    neighbors = []
    for j in [-1, 1]:
        offset = (j, 0, 0)
        newkey = add3tuple(coords, offset)
        try:
            cand = dictionary[newkey]
            neighbors.append(cand)
        except:
            pass
    for j in [-1, 1]:
        offset = (0, j, 0)
        newkey = add3tuple(coords, offset)
        try:
            cand = dictionary[newkey]
            neighbors.append(cand)
        except:
            pass
    for j in [-1, 1]:
        offset = (0, 0, j)
        newkey = add3tuple(coords, offset)
        try:
            cand = dictionary[newkey]
            neighbors.append(cand)
        except:
            pass
    return neighbors


cubes = dict()
for coords in read:
    coords = coords.strip().split(",")
    for i in range(len(coords)):
        coords[i] = int(coords[i])
    new_cube = Cube(coords)
    cubes.update({tuple(coords): new_cube})

for key in cubes:
    currentCube = cubes[key]
    neighbor_list = checkNeighbor(key, cubes)
    for cube in neighbor_list:
        cube.addNeighbor(currentCube)
        currentCube.addNeighbor(cube)

surface_area = 0
for key in cubes:
    current = cubes[key]
    current.updateSA()
    surface_area = surface_area + current.getSA()
print(surface_area)
