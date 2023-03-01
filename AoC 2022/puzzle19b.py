import re
from collections import deque, defaultdict
import copy
import time


class Node:
    def __init__(self, symbol, parent=None, path=[], time=32):
        self.parent = parent
        self.symbol = symbol
        self.children = None
        self.path = path
        self.time = time
        self.bots = []
        self.resources = []

    def setBots(self, bots):
        self.bots = bots

    def setResources(self, res):
        self.resources = res

    def setChildren(self, children):
        self.children = children

    def setPathVal(self, val):
        self.pathval = val

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def getName(self):
        return self.symbol

    def getPath(self):
        return self.path

    def getPathVal(self):
        return self.pathval

    def getTime(self):
        return self.time

    def getBots(self):
        return self.bots

    def getResources(self):
        return self.resources


class Blueprint:
    def __init__(self, number, orecost, claycost, obscost, geocost):
        self.number = number
        self.orecost = orecost
        self.claycost = claycost
        self.obscost = obscost
        self.geocost = geocost

    def getOreCost(self):
        return self.orecost

    def getClayCost(self):
        return self.claycost

    def getObsCost(self):
        return self.obscost

    def getGeoCost(self):
        return self.geocost

    def getCosts(self):
        return [self.orecost, self.claycost, self.obscost, self.geocost]

    def getName(self):
        return self.number


class Gamestate:
    def __init__(self, costs, bots=[1, 0, 0, 0], resources=[0, 0, 0, 0], time=32):
        self.costs = costs
        self.bots = bots
        self.resources = resources
        self.time = time
        self.turn = 1

    def build(self, bot):
        botlist = self.getBots()
        costs = self.getCosts()
        resources = self.getResources()
        match bot:
            case "O":
                newbot = [1, 0, 0, 0]
                buildcosts = [costs[0], 0, 0, 0]
            case "C":
                newbot = [0, 1, 0, 0]
                buildcosts = [costs[1], 0, 0, 0]
            case "Obs":
                newbot = [0, 0, 1, 0]
                buildcosts = [costs[2][0], costs[2][1], 0, 0]
            case "Geo":
                newbot = [0, 0, 0, 1]
                buildcosts = [costs[3][0], 0, costs[3][1], 0]
        if arrayComp(buildcosts, resources):
            resources = arrayMinus(resources, buildcosts)

            botresult = arraySum(botlist, newbot)
            self.bots = botresult
            self.resources = resources
            return True
        else:
            return False

    def wait(self, bot):
        costs = self.getCosts()
        resources = self.getResources()
        match bot:
            case "O":
                newbot = [1, 0, 0, 0]
                buildcosts = [costs[0], 0, 0, 0]
            case "C":
                newbot = [0, 1, 0, 0]
                buildcosts = [costs[1], 0, 0, 0]
            case "Obs":
                newbot = [0, 0, 1, 0]
                buildcosts = [costs[2][0], costs[2][1], 0, 0]
            case "Geo":
                newbot = [0, 0, 0, 1]
                buildcosts = [costs[3][0], 0, costs[3][1], 0]
        while arrayComp(buildcosts, resources) == False:
            self.update()
            resources = self.getResources()

    def update(self):
        bots = self.getBots()
        resources = self.getResources()
        self.time = self.time - 1
        self.turn = self.turn + 1
        result = arraySum(resources, bots)
        self.resources = result

    def getTime(self):
        return self.time

    def getBots(self):
        return self.bots

    def getResources(self):
        return self.resources

    def getCosts(self):
        return self.costs

    def getTurn(self):
        return self.turn


def arraySum(arr1, arr2):
    arr3 = list(map(lambda x, y: x + y, arr1, arr2))
    return arr3


def arrayMinus(arr1, arr2):
    arr3 = list(map(lambda x, y: x - y, arr1, arr2))
    return arr3


def arrayComp(costs, resources):
    for i in range(len(costs)):
        if costs[i] > resources[i]:
            return False
    return True


REGPARSE = re.compile(
    r"Blueprint (\d+): "
    r"Each ore robot costs (\d+) ore. "
    r"Each clay robot costs (\d+) ore. "
    r"Each obsidian robot costs (\d+) ore and (\d+) clay. "
    r"Each geode robot costs (\d+) ore and (\d+) obsidian."
)

SAMPLE_INPUT = [
    "Blueprint 1:Each ore robot costs 4 ore.Each clay robot costs 2 ore.Each obsidian robot costs 3 ore and 14 clay.Each geode robot costs 2 ore and 7 obsidian.\n",
    "Blueprint 2:Each ore robot costs 2 ore.Each clay robot costs 3 ore.Each obsidian robot costs 3 ore and 8 clay.Each geode robot costs 3 ore and 12 obsidian.",
]


def reparse(lines):
    return {
        (parse := re.match(REGPARSE, line)).group(1): [
            int(parse.group(2)),
            int(parse.group(3)),
            [int(parse.group(4)), int(parse.group(5))],
            [int(parse.group(6)), int(parse.group(7))],
        ]
        for line in lines
    }


def blueprint2model(bloop):
    ore_cost_list = [
        bloop.getOreCost(),
        bloop.getClayCost(),
        bloop.getObsCost()[0],
        bloop.getGeoCost()[0],
    ]
    max_ore = max(ore_cost_list)
    max_clay = bloop.getObsCost()[1]
    max_obs = bloop.getGeoCost()[1]
    return [max_ore, max_clay, max_obs]


def impPathB(node, bloop):
    timez = node.getTime()
    value = node.getResources()[-1]
    sum = value + (timez * (timez + 1)) // 2
    return sum


def impossiblePath(node, bloop):
    costs = bloop.getCosts()
    timez = node.getTime()
    resourc = copy.copy(node.getResources())
    botz = copy.copy(node.getBots())
    game = Gamestate(costs, bots=botz, resources=resourc, time=timez)
    actual_sum = 0
    impossible_sum = 0
    validity = False
    if game.getTime() < 0:
        return impossible_sum, validity, game.getTime()
    resource = game.getResources()
    resource[0] = 9999
    resource[1] = 9999
    ObsBuildable = False
    GeoBuildable = False
    while game.getTime() > 0:
        resource = game.getResources()

        geobuildcosts = [costs[3][0], 0, costs[3][1], 0]

        if arrayComp(geobuildcosts, resource):
            GeoBuildable = True

        else:
            GeoBuildable = False

        if GeoBuildable:
            game.build("Geo")
            game.update()
        else:
            game.build("Obs")
            game.update()

    resource = game.getResources()

    geodes = resource[-1]
    final_time = game.getTime()
    impossible_sum = geodes
    validity = True
    return impossible_sum, validity, final_time


def initGraph(bloop):

    symbols = ["O", "C", "Obs", "Geo"]
    max_vals = blueprint2model(bloop)
    max_val_dict = dict()
    costs = bloop.getCosts()
    sumz = sum(max_vals)
    max_val_dict.update({"O": max_vals[0] - 1})
    max_val_dict.update({"C": max_vals[1]})
    max_val_dict.update({"Obs": max_vals[2]})
    max_val_dict.update({"Geo": sumz})
    biggest = 0
    # print(max_vals)
    for val in max_vals:
        if val > biggest:
            biggest = val
    biggest = 30

    depth = 0
    initialNode = Node("root")
    initialNode.setBots([1, 0, 0, 0])
    initialNode.setResources([0, 0, 0, 0])
    levels = []
    levels.append(initialNode)
    Added = True
    best = 0
    bestpath = initialNode
    bestupdates = 0
    while depth < biggest and Added:
        # print(levels)
        newlevels = []
        added = False
        for vert in levels:
            # print(vert.getName())
            if vert.getTime() <= 0:
                continue
            children = []
            for sym in symbols:
                # print(sym)
                newpath = copy.copy(vert.getPath())
                newpath.append(sym)
                # print(newpath)
                try:
                    geoindex = newpath.index("Geo")
                except:
                    geoindex = 10000
                try:
                    obsindex = newpath.index("Obs")
                except:
                    obsindex = 9999
                try:
                    clayindex = newpath.index("C")
                except:
                    clayindex = 9998

                if obsindex < clayindex:
                    # print("line 309")
                    continue
                if geoindex < obsindex:
                    # print("line 310")
                    continue
                if newpath.count(sym) > max_val_dict[sym]:
                    # print("line 317")
                    continue

                # EVERYTHING
                # ABOVE
                # IS GOOD

                timez = vert.getTime()
                botz = copy.copy(vert.getBots())
                resourc = copy.copy(vert.getResources())

                game = Gamestate(costs, bots=botz, resources=resourc, time=timez)

                game.wait(sym)
                game.update()
                game.build(sym)

                newTime = game.getTime()

                if newTime < 0:
                    continue
                newBots = game.getBots()
                newResourc = game.getResources()

                newNode = Node(symbol=sym, parent=vert, path=newpath, time=newTime)
                newNode.setBots(newBots)
                newNode.setResources(newResourc)

                x = newNode.getResources()[-1]
                if bestupdates > 2:
                    lengthbranch = len(newNode.getPath())
                    bestlength = len(bestpath.getPath())
                    branchgeodes = newNode.getResources()[-1]
                    if lengthbranch >= bestlength:
                        if branchgeodes + 3 < best:
                            continue

                # impsum=impPathB(newNode,bloop)
                impsum, thing1, thing2 = impossiblePath(newNode, bloop)
                if impsum >= best:

                    children.append(newNode)

                    added = True
                    if newNode.getTime() >= 0 and sym == "Geo":
                        # actualnode=copy.deepcopy(newNode)
                        geodebots = newNode.getBots()[-1]
                        timeleft = newNode.getTime()

                        actual = newNode.getResources()[-1] + timeleft * geodebots

                        actualnode = Node(
                            newNode.getName(),
                            newNode.getParent(),
                            path=newNode.getPath(),
                            time=0,
                        )
                        actualnode.setResources([0, 0, 0, actual])
                        if actual > best:
                            # print("line 342")
                            # print(actual)
                            best = actual
                            bestpath = actualnode
                            # print(bestpath.getPath())
                            # print("impsum")
                            # print(impsum)
                            # print("timeleft")
                            # print(timeleft)
                            # print("res comp")
                            # print(newNode.getResources())
                            # print(actualnode.getResources())

                else:
                    continue

            vert.setChildren(children)
            newlevels.extend(children)
        levels = newlevels
        depth += 1

    return best, bestpath


file = open("puzzle19.txt", "r")
read = file.readlines()
# for line in read:
# print(line)

blueprints = reparse(read)
# print(blueprints)
blueprint_scoring = []

blueprint_list = []
for k, v in blueprints.items():
    # print(v)
    bloop = Blueprint(int(k), v[0], v[1], v[2], v[3])
    blueprint_list.append(bloop)

blueprint_list = blueprint_list[0:3]
seq = ["C", "C", "O", "Obs", "O", "C", "C", "C", "Obs", "Geo", "Obs", "O", "Obs"]
# print(isValid(seq,bloop))
best_of_each = []
time1 = time.time()
for bloop in blueprint_list:
    bestval, bestpath = initGraph(bloop)
    best_of_each.append((bestval, bestpath))
    print(bloop.getName())
    print("best geodes:")
    print(bestval)
    print("best path:")
    print(bestpath.getPath())
    print("time")
    print(bestpath.getTime())
    print("\n")

prod = 1
for i in range(len(best_of_each)):
    print(best_of_each[i][0])
    quality = best_of_each[i][0]
    prod = prod * quality
print("Answer is:")
print(prod)
time2 = time.time()
print("That took")
print(time2 - time1)
