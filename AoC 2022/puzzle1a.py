file = open("puzzle1.txt", "r")
read = file.readlines()

arr = []
data = []
biggest = (0, 0)

count = 0
for line in read:
    if line == "\n":
        count += 1
        calorie_sum = sum(arr)
        data.append([count, calorie_sum])
        arr = []
        if calorie_sum >= biggest[1]:
            biggest = (count, calorie_sum)
        continue
    length = len(line)
    end = length - 1
    num = line[0:end]
    arr.append(int(line[0:end]))
print(biggest)
