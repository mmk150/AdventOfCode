file = open("puzzle6.txt", "r")
read = file.readlines()

message = read[0]


def startPacket(s):
    NotFound = True
    index = 0
    while NotFound:
        substring = s[index : index + 4]
        if len(set(substring)) < 4:
            index += 1
        else:
            NotFound = False
    cleaned_message = s[index + 4 :]
    return index + 4, cleaned_message


start, cleaned = startPacket(message)
print(start)
