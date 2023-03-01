file = open("puzzle2.txt", "r")
read = file.readlines()
score = 0
for line in read:
    line = line.strip()
    strategy = line[-1]
    opponent = line[0]
    match strategy:
        case "X":
            val = 0
            match opponent:
                case "A":
                    val = val + 3
                case "B":
                    val = val + 1
                case "C":
                    val = val + 2
        case "Y":
            val = 3
            match opponent:
                case "A":
                    val = val + 1
                case "B":
                    val = val + 2
                case "C":
                    val = val + 3
        case "Z":
            val = 6
            match opponent:
                case "A":
                    val = val + 2
                case "B":
                    val = val + 3
                case "C":
                    val = val + 1

    score = score + val
print(score)
