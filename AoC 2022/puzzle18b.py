import copy

file = open("puzzle18.txt", "r")
read = file.readlines()


class Cube:
    def __init__(self, center, isAir, isoutsideAir):
        self.center = center
        self.x = center[0]
        self.y = center[1]
        self.z = center[2]
        self.neighbors = set()
        self.exposed = 0
        self.isair = isAir
        self.isoutsideAir = isoutsideAir

    def addNeighbor(self, neighbor):
        N = self.neighbors
        N.add(neighbor)
        self.neighbors = N

    def isAir(self):
        return self.isair

    def isOutsideAir(self):
        return self.isoutsideAir

    def setOutsideAir(self):
        self.isoutsideAir = True

    def getNeighbors(self):
        return self.neighbors

    def getNumNeighbors(self):
        return len(self.neighbors)

    def getCenter(self):
        return self.center

    def updateSA(self):
        if self.isAir():
            self.exposed = 0
        else:
            neigh = self.getNeighbors()
            sum = 0
            for x in neigh:
                if x.isOutsideAir():
                    sum += 1
            self.exposed = sum

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
            new_cube = Cube(newkey, isAir=True, isoutsideAir=False)
            dictionary.update({newkey: new_cube})
    for j in [-1, 1]:
        offset = (0, j, 0)
        newkey = add3tuple(coords, offset)
        try:
            cand = dictionary[newkey]
            neighbors.append(cand)
        except:
            new_cube = Cube(newkey, isAir=True, isoutsideAir=False)
            dictionary.update({newkey: new_cube})
    for j in [-1, 1]:
        offset = (0, 0, j)
        newkey = add3tuple(coords, offset)
        try:
            cand = dictionary[newkey]
            neighbors.append(cand)
        except:
            new_cube = Cube(newkey, isAir=True, isoutsideAir=False)
            dictionary.update({newkey: new_cube})
    return neighbors


cubes = dict()
max_x = 0
max_y = 0
max_z = 0
for coords in read:
    coords = coords.strip().split(",")
    for i in range(len(coords)):
        coords[i] = int(coords[i]) + 5
    if coords[0] > max_x:
        max_x = coords[0]
    if coords[1] > max_y:
        max_y = coords[1]
    if coords[2] > max_z:
        max_z = coords[2]
    coords = tuple(coords)
    new_cube = Cube(coords, isAir=False, isoutsideAir=False)
    cubes.update({tuple(coords): new_cube})

# print("max")
# print(max_x)
# print(max_y)
# print(max_z)
max_x += 10
max_y += 10
max_z += 10


xarray = []
for x in range(max_x + 1):
    yarray = []
    for y in range(max_y + 1):
        zarray = []
        for z in range(max_z + 1):
            coords = (x, y, z)
            try:
                lavacubeatpoint = cubes[coords]
                zarray.append((1, lavacubeatpoint))
            except:
                new_cube = Cube(coords, isAir=True, isoutsideAir=False)
                cubes.update({coords: new_cube})
                zarray.append((0, new_cube))
        yarray.append(zarray)
    xarray.append(yarray)

DefinitelyOutsideAir = cubes[(max_x, max_y, max_z)]
doa = cubes[(0, 0, 0)]
doa_arr = [doa, DefinitelyOutsideAir]


def loop(doa_array):
    for x in doa_array:
        outside(cube)


def outside(doa):
    outsideAirList = [doa]
    visited = []
    count = 0
    while outsideAirList != []:
        count += 1
        current_cube = outsideAirList.pop(0)
        visited.append(current_cube)
        current_cube.setOutsideAir()
        current_neighbors = list(current_cube.getNeighbors())
        for cube in current_neighbors:
            if cube.isAir():
                if not cube.isOutsideAir():
                    if cube not in outsideAirList:
                        outsideAirList.append(cube)
                        # print(cube.getCenter())
    # for x in visited:
    # print(x.getCenter())


current_cubes = copy.deepcopy(cubes)
for key in current_cubes:
    currentCube = cubes[key]
    neighbor_list = checkNeighbor(key, cubes)
    for cube in neighbor_list:
        cube.addNeighbor(currentCube)
        currentCube.addNeighbor(cube)


loop(doa_arr)
surface_area = 0
for key in cubes:
    current = cubes[key]
    current.updateSA()
    # print("Is Air?")
    # print(current.isAir())
    # print("Is outside air?")
    # print(current.isOutsideAir())
    # print("SA:")
    # print(current.getSA())
    surface_area = surface_area + current.getSA()
print(surface_area)
