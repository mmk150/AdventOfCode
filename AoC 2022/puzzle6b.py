file = open("puzzle6.txt", "r")
read = file.readlines()

message = read[0]


def startPacket(s):
    NotFound = True
    index = 0
    while NotFound:
        substring = s[index : index + 14]
        if len(set(substring)) < 14:
            index += 1
        else:
            NotFound = False
    cleaned_message = s[index + 14 :]
    return index + 14, cleaned_message


start, cleaned = startPacket(message)
print(start)
