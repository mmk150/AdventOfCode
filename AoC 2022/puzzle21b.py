import cmath


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

    def setFunc(self, functions):
        self.function = functions

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
        operation = complex(float(operation), 0)
        new_monkey = Monkey(name, value=operation)
        Monkeys.update({new_monkey: new_monkey.getFunc})
    else:
        line = read[i]
        monkey, expression = line.split(":")
        expression = expression.strip()
        var1, op, var2 = expression.split(" ")
        new_monkey = Monkey(name, function=[var1, op, var2])
        pre_Monkeys.append(new_monkey)

humn = Monkey("humann", value=complex(0, 1))
for monkey in Monkeys:
    if monkey.getName() == "humn":
        val = complex(0, 1)
        monkey.setVal(val)
for monkey in pre_Monkeys:
    if monkey.getName() == "root":
        func = monkey.getFunc()
        func[1] = "="
        monkey.setFunc(func)

# print(humn.getVal())
# print(humn.getFunc())


while pre_Monkeys != []:
    current = pre_Monkeys.pop(0)
    is_done = False
    # print(current.getName())
    # print(current.getFunc())
    for x in Monkeys:
        if x.getName() in current.getFunc():
            # print("line 66")
            current.replaceF(x.getName(), x.getVal())
    funcs = current.getFunc()
    if not isinstance(funcs[0], str) and not isinstance(funcs[2], str):
        if current.getName() == "root":
            Monkeys.update({current: current.getFunc()})
            is_done = True
        else:
            # print(f'{funcs[0]}{funcs[1]}{funcs[2]}')
            value = eval(f"{funcs[0]}{funcs[1]}{funcs[2]}")
            # print(current.getName())
            # print(value)
            current.setVal(value)
            Monkeys.update({current: current.getVal()})
            is_done = True
    if not is_done:
        pre_Monkeys.append(current)


side2 = 0
side1 = complex(0, 0)
for x in Monkeys:
    if x.getName() == "root":
        print("Root's value:")
        print(x.getFunc())
        print(x.getVal())
        values = x.getFunc()
        side2 = values[2].real
        side1 = values[0]
ans = (side2 - side1.real) / side1.imag
print("Answer:")
print(ans)


# for monk in Monkeys:
# print(monk.getName())
# print(monk.getFunc())
