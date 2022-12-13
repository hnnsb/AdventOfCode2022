from aocd.models import Puzzle
from os.path import basename
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
TEST = False
# -----------------------------------------------------
data = puzzle.input_data.split("\n\n")
if TEST:
    with open(f"day{day}/test.txt", "r") as f:
        data = f.read().split("\n\n")

for i, line in enumerate(data):
    data[i] = line.split("\n")
    for j, packet in enumerate(data[i]):
        data[i][j] = eval(packet)


def checkPackagePair(one, two):
    if type(one) == int and type(two) == int:
        if one == two:
            return -1

        return one < two

    elif type(one) == list and type(two) == list:
        pos = 0
        while pos < len(one) and pos < len(two):
            res = checkPackagePair(one[pos], two[pos])
            if res != -1:
                return res
            pos += 1
        if pos >= len(one) and pos < len(two):
            return True
        elif pos < len(one) and pos >= len(two):
            return False
        else:
            return -1
    # Mixed types
    elif type(one) == list and type(two) == int:
        return checkPackagePair(one, [two])
    elif type(one) == int and type(two) == list:
        return checkPackagePair([one], two)


result = 0
for i, pair in enumerate(data):
    if checkPackagePair(pair[0], pair[1]):
        result += i+1

print(result)
puzzle.answer_a = result

# Part 2
flatData = []
for pair in data:
    flatData.append(pair[0])
    flatData.append(pair[1])
flatData.append([[2]])
flatData.append([[6]])

# Sort packets
for n in range(len(flatData), 1, -1):
    for i in range(0, n-1):
        if not checkPackagePair(flatData[i], flatData[i+1]):
            flatData[i], flatData[i + 1] = flatData[i+1], flatData[i]
res = 1
for i, row in enumerate(flatData):
    if row == [[2]] or row == [[6]]:
        res *= i+1

print(res)
puzzle.answer_b = res
