file = open("puzzle9.txt", "r")
read = file.readlines()


# Change N for the difference between parts one and two
N = 10
knot_arr = []
for i in range(N):
    knot_arr.append((1024, 1024))


def differencev(head, tail):
    return (head[0] - tail[0], head[1] - tail[1])


def addv(head, tail):
    return (head[0] + tail[0], head[1] + tail[1])


def cmetric(head, tail):
    diff = differencev(head, tail)
    return max(abs(diff[0]), abs(diff[1]))


def knotnormalize(vec):
    N1 = max(abs(vec[0]), 1)
    N2 = max(abs(vec[1]), 1)
    return (vec[0] / N1, vec[1] / N2)


def simState(directions, knot_arr):
    tail_set = [knot_arr[-1]]
    head = knot_arr[0]
    while directions != []:
        x = directions[0]
        directions = directions[1:]
        match x:
            case "R":
                head = (head[0], head[1] + 1)
            case "L":
                head = (head[0], head[1] - 1)
            case "U":
                head = (head[0] - 1, head[1])
            case "D":
                head = (head[0] + 1, head[1])
        knot_arr[0] = head
        for i in range(len(knot_arr) - 1):
            delta = cmetric(knot_arr[i], knot_arr[i + 1])
            if delta > 1:

                temp = differencev(knot_arr[i], knot_arr[i + 1])

                temp = knotnormalize(temp)

                knot_arr[i + 1] = addv(knot_arr[i + 1], temp)

            tail_set.append(knot_arr[-1])

    tail_set = set(tail_set)
    return tail_set


directions = []
for line in read:
    x = line.split()
    num = int(x[1])
    for i in range(num):
        directions.append(x[0])

results = simState(directions, knot_arr)
print(results)
print(len(results))
