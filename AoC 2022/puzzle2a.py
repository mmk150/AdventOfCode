file = open("puzzle2.txt", "r")
read = file.readlines()
score = 0
for line in read:
    line = line.strip()
    if line[-1] == "X":
        val = 1
    elif line[-1] == "Y":
        val = 2
    else:
        val = 3
    if (line == "A Y") or (line == "B Z") or (line == "C X"):
        val = val + 6
    if (line == "A X") or (line == "B Y") or (line == "C Z"):
        val = val + 3
    score = score + val
print(score)
