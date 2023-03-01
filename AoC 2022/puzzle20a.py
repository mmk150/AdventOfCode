file = open("puzzle20.txt", "r")
read = file.readlines()


class FakeInt:
    def __init__(self, value):
        self.value = value

    def getVal(self):
        return self.value


class Wrapped:
    def __init__(self, length, arr):
        self.length = length
        self.arr = arr

    def Mix(self, a, current_index):
        modulus = self.length - 1
        temp = a.getVal()
        target = (temp + current_index + modulus) % modulus

        # print("mixing:")
        # print(temp)
        # print("in index:")
        # print(current_index)
        # print("target")
        # print(target)
        arr = self.arr
        arr.pop(current_index)
        arr.insert(target, a)
        # print("arr")
        # for x in arr:
        # print(x.getVal(), end= ",")
        # print("\n")
        return target

    def getArr(self):
        return self.arr


def sgn(a):
    if a < 0:
        return -1
    if a == 0:
        return 0
    else:
        return 1


def calcMod(index1, mod):
    dist = index1
    first = (1000 + index1) % mod
    second = (2000 + index1) % mod
    third = (3000 + index1) % mod
    return [first, second, third]


arr1 = []
indices_arr = []

for i in range(len(read)):
    num = int(read[i])
    num = FakeInt(num)
    arr1.append(num)
    indices_arr.append((num, i))


wrapped_arr = Wrapped(len(arr1), arr1)

for i in range(len(indices_arr)):
    tup = indices_arr[i]
    before = tup[1]
    arr = wrapped_arr.getArr()
    after = wrapped_arr.Mix(tup[0], arr.index(tup[0]))


modulus = len(arr1)
final_arr = wrapped_arr.getArr()
zero_ind = -1
for x in final_arr:
    if x.getVal() == 0:
        zero_ind = final_arr.index(x)

destinations = calcMod(zero_ind, modulus)
sum = 0
for x in destinations:
    sum += final_arr[x].getVal()
arrayz = []
for x in final_arr:
    arrayz.append(x.getVal())
print(arrayz)
print("sum is:")
print(sum)
print(modulus)
print(len(final_arr))
print(destinations)

# print(final_arr)
