file = open("puzzle7.txt", "r")
read = file.readlines()


class DirNode:
    def __init__(self, name=None, parent_dir=None, children_dir=None, files=None):
        self.name = name
        self.parent_dir = parent_dir
        self.children_dir = children_dir
        self.files = files
        self.size = 0
        self.locked = 0

    def get_name(self):
        return self.name

    def get_parent_dir(self):
        return self.parent_dir

    def get_children_dir(self):
        return self.children_dir

    def get_files(self):
        return self.files

    def set_parent_dir(self, p):
        if self.locked == 0:
            self.parent_dir = p

    def set_files(self, f):
        if self.locked == 0:
            self.files = f

    def set_children_dir(self, c):
        if self.locked == 0:
            self.children_dir = c

    def lock(self):
        self.locked = 1

    def set_size(self, s):
        self.size = s

    def get_size(self):
        return self.size


def list2DirNode(stringarr):
    directories = []
    files = []
    for line in stringarr:
        first = line[0]
        match first:
            case "dir":
                directories.append(line[1])
            case other:
                files.append(line)
    return directories, files


def DirectInit(current, direct_arr):
    NodeArr = []
    for x in direct_arr:
        temp = DirNode(name=x, parent_dir=current)
        NodeArr.append(temp)
    return NodeArr


def getNode(node, string):
    # print("Running getnode")
    # print(node.get_name())
    # print(node.get_children_dir()[0].get_name())
    children = node.get_children_dir()
    # print(children)
    if children == None:
        # print("Line")
        return None
    else:
        for x in children:
            if x.get_name() == string:
                return x


length = len(read)
base_node = DirNode(name="/")
current = base_node
dirArr = [base_node]

for i in range(length):
    read[i] = read[i].split()

for i in range(length):
    line = read[i]
    # print(line)
    if line[0] == "$":
        match line[1]:
            case "cd":
                if line[2] == "/":
                    current = base_node
                    continue
                if line[2] == "..":
                    current = current.get_parent_dir()
                    continue
                else:
                    # print("Line 87 debug")
                    # print(line)
                    # print(current.get_name())
                    # print(current.get_children_dir())
                    current = getNode(current, line[2])
                    # print("CD to" + current.get_name())
                    continue
            case "ls":
                for j in range(i + 1, length):
                    # print(read[j])
                    if read[j][0] == "$":
                        directories, files = list2DirNode(read[i + 1 : j])
                        directories = DirectInit(current, directories)
                        dirArr.extend(directories)
                        if directories != []:
                            current.set_children_dir(directories)
                            # print("Line 100")
                            # print(current.get_name())
                            # print(current.get_children_dir())

                        if files != []:
                            current.set_files(files)
                            sum = 0
                            for x in files:
                                sum = sum + int(x[0])
                            current.set_size(sum)
                        current.lock()
                        i = j - 1
                        break
                    if j == length - 1:
                        directories, files = list2DirNode(read[i + 1 :])
                        directories = DirectInit(current, directories)
                        dirArr.extend(directories)
                        if directories != []:
                            current.set_children_dir(directories)
                            # print("Line 100")
                            # print(current.get_name())
                            # print(current.get_children_dir())

                        if files != []:
                            current.set_files(files)
                            sum = 0
                            for x in files:
                                sum = sum + int(x[0])
                            current.set_size(sum)
                        current.lock()
                        i = j - 1
                        break


def SizeAdj(node):
    next = node.get_children_dir()
    sum = node.get_size()
    if next == None:
        return sum
    else:
        for x in next:
            sum = sum + SizeAdj(x)
        return sum


sum = 0
for x in dirArr:
    # print(x.get_name())
    x.set_size(SizeAdj(x))
    # print(x.get_size())
    if x.get_size() <= 100000:
        sum = sum + x.get_size()
print(sum)


max = 70000000
min = 30000000

delta = max - base_node.get_size()
needed_space = min - delta

dirArr.sort(key=lambda node: node.get_size())

for x in dirArr:
    if x.get_size() > needed_space:
        print(x.get_name() + " " + str(x.get_size()))
        break
