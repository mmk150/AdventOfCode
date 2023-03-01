file = open("puzzle21.txt", "r")
read = file.readlines()


class Monkey:
    def __init__(self, name, value=0, function=[]) -> None:
        self.name = name
        self.value = value
        self.function = function

    def getName(self):
        return self.name

    def getFunc(self):
        return self.function

    def getVal(self):
        return self.value

    def setVal(self, val):
        self.value = val

    def replaceF(self, var_name, value):
        arr = self.getFunc()
        for i in range(len(arr)):
            if arr[i] == var_name:
                arr[i] = value
        self.function = arr


Monkeys = dict()
pre_Monkeys = []
for i in range(len(read)):
    line = read[i].strip()
    line = line.split(":")
    # print(line)
    name = line[0]
    func_text = line[1].strip()
    # print(func_text)
    operation = func_text
    if operation.isdigit():
        operation = float(operation)
        new_monkey = Monkey(name, value=operation)
        Monkeys.update({new_monkey: new_monkey.getFunc})
    else:
        line = read[i]
        monkey, expression = line.split(":")
        expression = expression.strip()
        var1, op, var2 = expression.split(" ")
        new_monkey = Monkey(name, function=[var1, op, var2])
        pre_Monkeys.append(new_monkey)

while pre_Monkeys != []:
    current = pre_Monkeys.pop(0)
    is_done = False
    print(current.getName())
    print(current.getFunc())
    for x in Monkeys:
        if x.getName() in current.getFunc():
            # print("line 66")
            current.replaceF(x.getName(), x.getVal())
    funcs = current.getFunc()
    if isinstance(funcs[0], float) and isinstance(funcs[2], float):
        print(f"{funcs[0]}{funcs[1]}{funcs[2]}")
        value = eval(f"{funcs[0]}{funcs[1]}{funcs[2]}")
        print(current.getName())
        print(value)
        current.setVal(value)
        Monkeys.update({current: current.getVal()})
        is_done = True
    if not is_done:
        pre_Monkeys.append(current)

for x in Monkeys:
    if x.getName() == "root":
        print("Root's value:")
        print(x.getVal())


# for monk in Monkeys:
# print(monk.getName())
# print(monk.getFunc())
