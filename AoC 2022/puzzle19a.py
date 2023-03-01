import re
from collections import deque
import copy


class Node:
    def __init__(self, symbol, parent=None, path=[], pathval=0, time=24):
        self.parent = parent
        self.symbol = symbol
        self.children = None
        self.path = path
        self.pathval = pathval
        self.time = time
        self.bots
        self.resources

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
    def __init__(self, costs, bots=[1, 0, 0, 0], resources=[0, 0, 0, 0], time=24):
        self.costs = costs
        self.bots = [1, 0, 0, 0]
        self.resources = [0, 0, 0, 0]
        self.time = 24
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
            # print('line 51')
            # print(resources)
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


def impossiblePath(node, bloop):
    patharr = node.getPath()
    costs = bloop.getCosts()
    game = Gamestate(costs)
    actual_sum = 0
    impossible_sum = 0
    validity = False
    for x in patharr:
        game.wait(x)
        if game.build(x):
            game.update()
        else:
            # print("line 186")
            return impossible_sum, validity, game.getTime()
    if game.getTime() < 0:
        # print("line 189")
        return impossible_sum, validity, game.getTime()
    resource = game.getResources()
    resource[0] = 9999
    ObsBuildable = False
    GeoBuildable = False
    while game.getTime() > 0:
        resource = game.getResources()
        # print(game.getResources())
        obsbuildcosts = [costs[2][0], costs[2][1], 0, 0]
        geobuildcosts = [costs[3][0], 0, costs[3][1], 0]
        # print("geobuildcosts")
        # print(geobuildcosts)
        if arrayComp(geobuildcosts, resource):
            GeoBuildable = True
            # print("Line 199")
        else:
            GeoBuildable = False

        if arrayComp(obsbuildcosts, resource):
            ObsBuildable = True
        else:
            ObsBuildable = False

        if GeoBuildable:
            game.build("Geo")
            game.update()
        else:
            if ObsBuildable:
                game.build("Obs")
                game.update()
            else:
                game.build("C")
                game.update()

    resource = game.getResources()

    geodes = resource[-1]
    time = game.getTime()
    impossible_sum = geodes
    validity = True
    return impossible_sum, validity, time


def botsOverMax(node, maxvals):
    path = node.getPath()
    # print(path)
    ore_max = maxvals[0]
    clay_max = maxvals[1]
    obs_max = maxvals[2]
    ore_count = path.count("O")
    # print("orecount")
    # print(ore_count)
    if ore_count > ore_max:
        return True
    clay_count = path.count("C")
    # print("claycount")
    # print(clay_count)
    if clay_count > clay_max:
        return True
    # print("obscount")
    obs_count = path.count("Obs")
    if obs_count > obs_max:
        return True
    return False


def initGraph(bloop):
    best = 0
    bestpath = None
    symbols = ["O", "C", "Obs", "Geo"]
    max_vals = blueprint2model(bloop)
    max_val_dict = dict()
    sumz = sum(max_vals)
    max_val_dict.update({"O": max_vals[0]})
    max_val_dict.update({"C": max_vals[1] / 2})
    max_val_dict.update({"Obs": max_vals[2]})
    max_val_dict.update({"Geo": sumz})
    biggest = 0
    print(max_vals)
    for val in max_vals:
        if val > biggest:
            biggest = val
    biggest += 2

    depth = 0
    initialNode = Node("root")
    levels = deque()
    levels.append(initialNode)
    Added = True
    while depth < biggest and Added:
        newlevels = []
        for vert in levels:
            children = []
            added = False
            for sym in symbols:
                newpath = copy.copy(vert.getPath())
                newpath.append(sym)
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
                    continue
                if geoindex < obsindex:
                    continue
                if newpath.count(sym) > max_val_dict[sym]:
                    continue

                newNode = Node(sym, parent=vert, path=newpath)
                imp, valid, time = impossiblePath(newNode, bloop)
                # print("imp")
                # print(imp)
                # print("valid")
                # print(valid)
                # print("time")
                # print(time)
                if valid and imp > best:
                    # print("line 275")
                    # print(newpath)
                    children.append(newNode)
                    Added = True
                    if geoindex != 10000:
                        actual, valid, time = isValid(newNode.getPath(), bloop)
                        if actual > best:
                            print("Line 281")
                            print(" ")
                            best = actual
                            bestpath = newNode
                            print(best)
                            print(bestpath.getPath())
                else:
                    continue
            vert.setChildren(children)
            newlevels.extend(children)
        levels = newlevels
        depth += 1
    print("Initgraph DONE")
    return bestpath, best


def bestOfAll(bloop):
    bestpath, bestval = initGraph(bloop)
    return bestval, bestpath


def bestOfAllPossibleWorlds(bloop):
    best = 0
    best_path = []
    root_node = initGraph(bloop)
    max_vals = blueprint2model(bloop)
    biggest = 0

    for val in max_vals:
        if val > biggest:
            biggest = val

    def defaultval():
        return False

    open = deque()
    # closed=defaultdict(defaultval)
    open.append(root_node)

    while open:
        current = open.popleft()
        # closed.update({current:True})
        children = current.getChildren()
        for child in children:
            print("line 261")
            if botsOverMax(child, max_vals):
                print("line 263")
                continue
            imp_val, validity = impossiblePath(child, bloop)
            if not validity:
                print("line 266")
                continue
            if imp_val < best:
                print("line 269")
                continue
            else:
                print("line 272")
                childpath = child.getPath()
                actual_val, validity, time = isValid(childpath, bloop)
                open.append(child)
                if actual_val > best:
                    best = actual_val
                    best_path = childpath

    return best, best_path


def isValid(build_seq, blueprint):
    time = -1
    bloop = blueprint
    costs = bloop.getCosts()
    game = Gamestate(costs)
    actual = -1
    for x in build_seq:
        game.wait(x)
        # print("2build:")
        # print(x)
        # print("current time")
        # print(game.getTurn())
        # print("resources")
        # print(game.getResources())
        # print("botlist:")
        # print(game.getBots())
        # print(build_seq)
        game.update()
        # print("line 150")
        if game.getTime() < 0:
            # print("line 178")
            print(x)
            return actual, False, time
        res = game.build(x)

        if res == False:
            # print("line 182")
            return actual, False, time
    timey = game.getTime()
    while game.getTime() > 0:
        game.update()
    actual = game.getResources()[-1]
    return actual, True, timey


def computeScore(path):
    pass


file = open("puzzle19test.txt", "r")
read = file.readlines()
for line in read:
    print(line)

blueprints = reparse(read)
print(blueprints)
blueprint_scoring = []

blueprint_list = []
for k, v in blueprints.items():
    print(v)
    bloop = Blueprint(int(k), v[0], v[1], v[2], v[3])
    blueprint_list.append(bloop)

bloop = blueprint_list[1]
seq = [
    "O",
    "O",
    "C",
    "C",
    "C",
    "C",
    "C",
    "Obs",
    "Obs",
    "Obs",
    "Obs",
    "Obs",
    "Geo",
    "Geo",
]
print(isValid(seq, bloop))
best_of_each = []
