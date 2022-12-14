from functools import cmp_to_key
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


def checkPackagePair(one: int | list, two: int | list):
    if isinstance(one, int) and isinstance(two, int):
        if one < two:
            return -1
        elif one > two:
            return 1
        else:
            return 0

    elif isinstance(one, list) and isinstance(two, list):
        pos = 0
        while pos < len(one) and pos < len(two):
            res = checkPackagePair(one[pos], two[pos])
            if res != 0:
                return res
            pos += 1
        if pos >= len(one) and pos < len(two):
            return -1
        elif pos < len(one) and pos >= len(two):
            return 1
        else:
            return 0
    # Mixed types
    elif isinstance(one, list) and isinstance(two, int):
        return checkPackagePair(one, [two])
    elif isinstance(one, int) and isinstance(two, list):
        return checkPackagePair([one], two)

    assert False


res = 0
for i, pair in enumerate(data):
    if checkPackagePair(pair[0], pair[1]) == -1:
        res += i+1

print(res)
puzzle.answer_a = res

# Part 2
flatData = []
for pair in data:
    flatData.append(pair[0])
    flatData.append(pair[1])
flatData.append([[2]])
flatData.append([[6]])

flatData = sorted(flatData, key=cmp_to_key(checkPackagePair))
res = 1
for i, row in enumerate(flatData):
    if row == [[2]] or row == [[6]]:
        res *= i+1

print(res)
puzzle.answer_b = res
