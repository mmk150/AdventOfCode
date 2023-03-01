import time

start = time.time()

file = open("puzzle20.txt", "r")
read = file.readlines()


class FakeInt:
    def __init__(self, value, modulus):
        self.value = value
        self.modulus = modulus
        self.remainder = 0
        self.reduced = 0

    def getVal(self):
        return self.value

    def setVals(self):
        self.reduced = self.getVal() // self.modulus
        self.remainder = self.getVal() % self.modulus

    def getRed(self):
        return self.reduced

    def getRem(self):
        return self.remainder

    def getMod(self):
        return self.modulus


class Wrapped:
    def __init__(self, length, arr):
        self.length = length
        self.arr = arr

    def Mix(self, a, current_index):
        modulus = a.getMod()
        temp = a.getRem()
        target = (temp + current_index + modulus) % modulus
        # print("mixing:")
        # print(a.getVal())
        # print("whose remainder is:")
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


# bigprime=1
bigprime = 811589153
arr1 = []
indices_arr = []
modulus = len(read) - 1


for i in range(len(read)):
    num = int(read[i]) * bigprime
    num = FakeInt(num, modulus)
    num.setVals()
    arr1.append(num)
    indices_arr.append(num)


count = 0
wrapped_arr = Wrapped(len(arr1), arr1)
arr = wrapped_arr.getArr()


arr = wrapped_arr.getArr()

count = 0
while count < 10:
    for i in range(len(indices_arr)):
        fake_int = indices_arr[i]
        arr = wrapped_arr.getArr()
        after = wrapped_arr.Mix(fake_int, arr.index(fake_int))
    # for x in arr:
    # print(x.getVal(),end=",")
    # print("\n")
    count += 1


final_arr = wrapped_arr.getArr()


zero_ind = -1
for x in final_arr:
    if x.getVal() == 0:
        zero_ind = final_arr.index(x)

destinations = calcMod(zero_ind, modulus + 1)
sum = 0
for x in destinations:
    sum += final_arr[x].getVal()
arrayz = []
# for x in final_arr:
# arrayz.append(x.getVal())
# print(arrayz)
print("sum is:")
print(sum)
print(modulus)
print(len(final_arr))
print(destinations)


# print(final_arr)
end = time.time()
print(end - start)
