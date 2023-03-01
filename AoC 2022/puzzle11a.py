file = open("puzzle11.txt", "r")
read = file.readlines()


class Monkey:
    def __init__(self, name, items, operation, testval, true_target, false_target):
        self.name = name
        self.items = items
        self.operation = operation
        self.testval = testval
        self.true_target = true_target
        self.false_target = false_target
        self.numberInspects = 0

    def getItems(self):
        return self.items

    def inspect(self):
        self.numberInspects += 1
        ite = self.items[0]
        self.items[0] = self.operation(ite) // 3

    def test(self):
        ite = self.items[0]
        if ite % self.testval == 0:
            return True
        else:
            return False

    def yeet(self, blorp):
        ite = self.items[0]
        self.items = self.items[1:]
        if blorp:
            return [ite, self.true_target]
        else:
            return [ite, self.false_target]

    def catch(self, ite):
        self.items.append(ite)
        return


def inputParser(arr):
    Monkeydata = []
    for line in read:
        if "Monkey" in line:
            line = line.strip()
            leng = len(line)
            line = line[0 : leng - 1]
            name = int(line.split()[-1])
        if "Starting" in line:
            x = line.split(":")[1]
            x = x.strip().split(",")
            items = [int(a) for a in x]
        if "Operation" in line:
            func_text = line.split("=")[1]
            func_text = func_text.strip()
            operation = eval(f"lambda old: {func_text}")
        if "Test" in line:
            divisor = int(line.split()[-1])
        if "true:" in line:
            true_target = int(line.split()[-1])
        if "false:" in line:
            false_target = int(line.split()[-1])
            Monkeydata.append(
                Monkey(name, items, operation, divisor, true_target, false_target)
            )
    return Monkeydata


Monkeys = inputParser(read)
zero = Monkeys[0]

rounds = 20

for j in range(rounds):
    for monk in Monkeys:
        items = monk.getItems()
        number_items = len(items)
        counter = 0
        while counter < number_items:
            monk.inspect()
            result = monk.test()
            yote_item, to_whom = monk.yeet(result)
            Monkeys[to_whom].catch(yote_item)
            counter += 1


Monkeys.sort(key=lambda m: 0 - m.numberInspects)
MoNkEyBuSiNeSs = Monkeys[0].numberInspects * Monkeys[1].numberInspects
print(MoNkEyBuSiNeSs)
