import math
import sys
from aocd.models import Puzzle
from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()

sys.setrecursionlimit(10000)

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
TEST = False
# -----------------------------------------------------
data = [list(row) for row in puzzle.input_data.splitlines()]
if TEST:
    with open(f"day{day}/test.txt", "r") as f:
        data = [list(row) for row in f.read().splitlines()]
start, end = (), ()
for i, row in enumerate(data):
    for j, c in enumerate(row):
        if c == "S":
            data[i][j] = 1
            start = (i, j)
        elif c == "E":
            data[i][j] = 26
            end = (i, j)
        else:
            data[i][j] = ord(c)-ord("a")+1

# Part 1
queue = [(start, 0)]
checked = set()
while queue:
    (i, j), dist = queue.pop(0)
    if (i, j) in checked:
        continue
    if (i, j) == end:
        print(dist)
        puzzle.answer_a = dist
        break
    checked.add((i, j))
    for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbour_i = i + ii
        neighbour_j = j + jj
        if 0 <= neighbour_i < len(data) and 0 <= neighbour_j < len(data[0]) and data[neighbour_i][neighbour_j] <= data[i][j] + 1:
            queue.append(((neighbour_i, neighbour_j), dist+1))

# Part 2
queue = [(start, 0)]
for i, row in enumerate(data):
    for j, c in enumerate(row):
        if c == 1:
            queue.append(((i,j),0))

checked = set()
while queue:
    (i, j), dist = queue.pop(0)
    if (i, j) in checked:
        continue
    if (i, j) == end:
        print(dist)
        puzzle.answer_b = dist
        break
    checked.add((i, j))
    for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbour_i = i + ii
        neighbour_j = j + jj
        if 0 <= neighbour_i < len(data) and 0 <= neighbour_j < len(data[0]) and data[neighbour_i][neighbour_j] <= data[i][j] + 1:
            queue.append(((neighbour_i, neighbour_j), dist+1))
