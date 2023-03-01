import itertools
import copy


class Valve:
    def __init__(self, name, rate) -> None:
        self.name = name
        self.tunnels = []
        self.pressure_rate = rate
        self.score = []
        self.distance = 1
        self.total_release = 0
        self.locked = True

    def getTotal(self):
        return self.total_release

    def getName(self):
        return self.name

    def getRate(self):
        return self.pressure_rate

    def getTunnels(self):
        return self.tunnels

    def getDistance(self):
        return self.distance

    def getScore(self):
        return self.weighted_score

    def getDens(self):
        return self.density

    def isLocked(self):
        return self.locked

    def isOpen(self):
        return not self.locked

    def setTunnels(self, tunnel_arr):
        self.tunnels = tunnel_arr

    def setDistance(self, distance):
        self.distance = distance

    def calcScore(self, time):
        return self.score[time]

    def initweightedscore(self):
        score = []
        for time in range(0, 31, 1):
            score.append(self.getRate() * time)
        self.score = score

    def calcWeightedScore(self, time, distance):
        if self.getRate() == 0:
            return 0
        else:
            return self.score[time - distance - 1] / (distance**2)

    def open(self, time):
        self.locked = False
        self.total_release = time * self.getRate()


def completeGraph(inc_graph):
    dist = dict()
    comp_graph = []
    for v in inc_graph:
        distances = BFS(v, inc_graph)
        for w in inc_graph:
            dist.update({(v, w): distances[w]})
    nonzero = []
    for j in inc_graph:
        if j.getRate() != 0:
            nonzero.append(j)
    for v in inc_graph:
        if v.getName() == "AA":
            nonzero.append(v)
            break
    for v in nonzero:
        others = []
        for z in nonzero:
            if z.getName() != v.getName():
                others.append((z, dist[(v, z)]))
        new_vertex = Valve(v.getName(), v.getRate())
        new_vertex.setTunnels(others)
        comp_graph.append(new_vertex)
    return comp_graph


def BFS(start, valves_list):
    distance = dict()
    for i in valves_list:
        distance.update({i: 0})
    que = []
    explored = [start]
    que.append(start)
    dist = 0
    while que != []:
        # print(que)
        vertex = que.pop(0)
        # print(vertex.getName())
        dist = distance[vertex] + 1
        edges = vertex.getTunnels()
        # print("line 87")
        # print(edges)
        for dest in edges:
            if dest not in explored:
                explored.append(dest)
                que.append(dest)
                distance.update({dest: dist})
    return distance


def getValve(valves_list, valve):
    for v in valves_list:
        if v.getName() == valve:
            return v


def checkSum(vlist, distances, time):
    sum = 0
    for i in range(len(vlist) - 1):
        dist = 0
        first = vlist[i]
        next = vlist[i + 1]
        dist = distances[(first.getName(), next.getName())] + 1
        sum = sum + dist + 1
    if sum <= time:
        return True
    else:
        return False


def checkValue(vlist, distances, time=30):
    score = 0
    time_spent = 0
    for i in range(len(vlist) - 1):
        dist = 0
        first = vlist[i]
        next = vlist[i + 1]
        dist = distances[(first.getName(), next.getName())] + 1
        time_spent = time_spent + dist
        # print(time-time_spent)
        score = score + next.calcScore(time - time_spent)
    return score


def checkMax(vlist, rest, time=30):
    score = 0
    time_spent = 0
    for i in range(len(vlist) - 1):
        dist = 0
        first = vlist[i]
        next = vlist[i + 1]
        dist = distances[(first.getName(), next.getName())] + 1
        time_spent = time_spent + dist
        score = score + next.calcScore(time - time_spent)
    sum = 0
    for x in rest:
        sum = sum + x.calcScore(time - time_spent)
    return score + sum


def heuristicRun(vlist, distances, time):
    vlist = copy.deepcopy(vlist)
    current = vlist.pop(-1)
    time = time
    tried = [current]
    score = 0
    while time >= 0:
        vlist.sort(
            key=lambda x: x.calcWeightedScore(
                time, distances[(current.getName(), x.getName())]
            )
        )
        next = vlist.pop(-1)
        dist = distances[(current.getName(), next.getName())]
        time = time - dist - 1
        if time < 0:
            break
        score += next.calcScore(time)
        current = next
        tried.append(current)

    return score, tried


def recursive(path, next, time, distances):
    # path is a list of graph node objects (that we have visited)
    # next is a list of graph node objects (we havent visited)
    # distances is a dict storing distances between nodes
    # time is an integer

    # bound is an int global variable
    # best is a global list of graph node objects of the best path found yet
    # count is a global int that counts how many times this runs
    global bound, best, count
    count += 1
    merp = ["lol"]
    if len(path) == 1:
        next_arr = itertools.combinations(next, 1)
        for item in next_arr:
            item = item[0]
            last = path[-1]
            dist = distances[last.getName(), item.getName()]
            derp = copy.copy(path)
            splerp = copy.copy(next)
            derp.append(item)
            splerp.remove(item)
            merp = recursive(derp, splerp, time - dist - 1, distances)

    value = checkValue(path, distances)
    if value > bound:
        bound = value
        best = path
        # print("Bound exceeded!")
        # print(bound)
        # print(len(path))
    elif checkMax(path, next) >= bound and next != []:
        next_arr = list(itertools.combinations(next, 1))
        for item in next_arr:
            item = item[0]
            last = path[-1]
            dist = distances[last.getName(), item.getName()]
            if time - dist - 1 > -1:
                derp = copy.copy(path)
                splerp = copy.copy(next)
                derp.append(item)
                splerp.remove(item)
                # print("line219")
                # for x in path:
                # print(x.getName())
                # print(time-dist-1)
                merp = recursive(derp, splerp, time - dist - 1, distances)
    if next == []:
        return merp


file = open("puzzle16.txt", "r")
read = file.readlines()

for i in range(len(read)):
    read[i] = read[i].split()
Valve_information = []
Valve_temp = []

for line in read:
    print(line)
    name = line[1]
    rate = line[4].split("=")[1]
    rate = rate.strip(";")
    tunnels = line[9:]
    for i in range(len(tunnels)):
        tunnels[i] = tunnels[i].strip(",")
    valve_info = [name, rate, tunnels]
    temp = Valve(name, int(rate))
    Valve_temp.append(temp)
    Valve_information.append(valve_info)

for i in range(len(Valve_temp)):
    v = Valve_temp[i]
    # print("line129")
    # print(v.getName())
    v_info = Valve_information[i]
    temp_list = []
    for name in v_info[2]:
        temp_list.append(getValve(Valve_temp, name))
    # print("line 133")
    # print(temp_list)
    v.setTunnels(temp_list)


complete_graph = completeGraph(Valve_temp)
total = copy.deepcopy(complete_graph)
time = 30
distances = dict()
for v in complete_graph:
    for w in complete_graph:
        for z in v.getTunnels():
            if z[0].getName() == w.getName():
                distances.update({(v.getName(), w.getName()): z[1]})

for v in complete_graph:
    v.initweightedscore()
    # print(v.calcWeightedScore(30,1))
    # print(v.getRate())


print(len(complete_graph))
print(" \n")
bound, best = heuristicRun(complete_graph, distances, time)
print(bound)
for v in best:
    print(v.getName())
count = 0
next = copy.deepcopy(complete_graph)
path = [next.pop(-1)]
print(path[0].getName())
time = 30
newpath = recursive(path, next, time, distances)

print(bound)
for x in best:
    print(x.getName())

print("count")
print(count)
