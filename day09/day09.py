from aocd.models import Puzzle
from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
import math
load_dotenv()

fileName = basename(__file__)
day = int(findall(r"[1-9]+", fileName)[0])
puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
TEST = False
# -----------------------------------------------------
data = puzzle.input_data.splitlines()
data = [row.split(" ") for row in puzzle.input_data.splitlines()]
if TEST:
    with open("day09/test.txt", "r") as f:
        data = f.read().splitlines()
        data = [row.split(" ") for row in data]
data = [(row[0], int(row[1])) for row in data]


def dist(h, t):
    return math.sqrt((h[0]-t[0])**2 + (h[1]-t[1])**2)


MAX_DIST = math.sqrt(2)

visited = set()
h = (0, 0)
t = (0, 0)
for dir, steps in data:
    for i in range(steps):
        h_old = h
        if dir == "U":
            h = (h_old[0], h_old[1]+1)
        if dir == "D":
            h = (h_old[0], h_old[1]-1)
        if dir == "L":
            h = (h_old[0]-1, h_old[1])
        if dir == "R":
            h = (h_old[0]+1, h_old[1])

        if dist(h, t) > MAX_DIST:
            t = h_old

        visited.add(t)

res = len(visited)
print("Part a: ", res)
puzzle.answer_a = res

visited = set()
ks = [(0, 0) for t in range(10)]
for dir, steps in data:
    for i in range(steps):
        h_old = tuple(ks[0])
        if dir == "U":
            ks[0] = (h_old[0], h_old[1]+1)
        if dir == "D":
            ks[0] = (h_old[0], h_old[1]-1)
        if dir == "L":
            ks[0] = (h_old[0]-1, h_old[1])
        if dir == "R":
            ks[0] = (h_old[0]+1, h_old[1])

        for i, k in enumerate(ks):
            if i == 0:
                continue
            dx = ks[i-1][0] - ks[i][0]
            dy = ks[i-1][1] - ks[i][1]

            if dx == 0 and abs(dy) == 2:
                dy = 1 if dy >= 0 else -1
                new_pos = (ks[i][0], ks[i][1]+dy)
                ks[i] = new_pos
            elif dy == 0 and abs(dx) == 2:
                dx = 1 if dx >= 0 else -1
                new_pos = (ks[i][0]+dx, ks[i][1])
                ks[i] = new_pos
            elif (abs(dx)+abs(dy) > 2):
                dx = 1 if dx >= 0 else -1
                dy = 1 if dy >= 0 else -1
                new_pos = (ks[i][0]+dx, ks[i][1]+dy)
                ks[i] = new_pos

        visited.add(ks[-1])

print("Part b: ", len(visited))
puzzle.answer_b = len(visited)
