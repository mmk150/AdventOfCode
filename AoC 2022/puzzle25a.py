import math

file = open("puzzle25.txt", "r")
read = file.readlines()


snafu_numbers = []
for line in read:
    num = []
    raw = line.strip()
    for c in raw:
        num.append(c)
    snafu_numbers.append(num)


def snafu2real(num_arr):
    sum = 0
    length = len(num_arr)
    for i in range(length - 1, -1, -1):
        place = num_arr.pop(0)
        if place in ["0", "1", "2"]:
            place = int(place)
            coeff = place
            power = 5**i
            sum = sum + (coeff * power)
        else:
            if place == "-":
                place = -1
                sum = sum + place * (5**i)
            if place == "=":
                place = -2
                sum = sum + place * (5**i)
    return sum


def convert_to_quinary(decimal_number):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % 5
        remainder_stack.append(remainder)
        decimal_number = decimal_number // 5

    digits = []
    while remainder_stack:
        digits.append(str(remainder_stack.pop()))

    return "".join(digits)


def quinary_to_snafu(quin_number):
    rev = list(quin_number)
    rev.reverse()

    digits = []
    carry = 0
    for x in rev:
        real_res = int(x) + carry
        carry = 0
        if real_res in [0, 1, 2]:
            digits.append(str(real_res))
        else:
            if real_res == 3:
                digits.append("=")
                carry = 1
            if real_res == 4:
                digits.append("-")
                carry = 1
            if real_res >= 5:
                rem = real_res % 5
                quot = real_res // 5
                carry = quot
                digits.append(str(rem))
    if carry > 0:
        digits.append(str(carry))

    digits.reverse()
    return digits


# print(snafu_numbers)
real_arr = [snafu2real(x) for x in snafu_numbers]
added = sum(real_arr)
# print(real_arr)
# print(added)

quin = convert_to_quinary(added)
# print(quin)

snafu_ans = quinary_to_snafu(quin)

# print("snafu")
# print(snafu_ans)
# print("check:")
# print("snafu back to real gives:")
snafu_to_real_num = snafu2real(snafu_ans)
# print(snafu_to_real_num)
# print("real originally was:")
# print(added)
# print("time to find the difference")
deal = snafu_to_real_num - added
# print(deal)

snafu_ans = quinary_to_snafu(convert_to_quinary(added))
# print(snafu_ans)
string_comp = ""
for x in snafu_ans:
    string_comp = string_comp + x
print(string_comp)
