file = open("puzzle5.txt", "r")
read = file.readlines()

index = 0
num_stacks = 0
arr = []

for line in read:
    if line.strip() == "":
        index += 1
        continue
    if line.find("move") != -1:
        last_line = arr[-1]
        num_stacks = int(last_line[-1])
        arr.pop()
        break
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace("    ", "  %  ")
    arr.append(line.split())
    index += 1

stacks = []

for i in range(num_stacks):
    temp = []
    stacks.append(temp)


for i in range(len(arr) - 1, -1, -1):
    for j in range(num_stacks):
        crate = arr[i][j]
        if crate != "%":
            stacks[j].append(crate)

directions = []

for line in read[index:]:
    line = line.split()
    direct = [int(line[1]), int(line[3]), int(line[5])]
    directions.append(direct)

for directs in directions:
    num_moves = directs[0]
    start = directs[1] - 1
    target = directs[2] - 1
    cratestack = []
    for i in range(num_moves):
        popped_crate = stacks[start].pop()
        cratestack.append(popped_crate)
    cratestack.reverse()
    stacks[target].extend(cratestack)

for items in stacks:
    print(items[-1])
