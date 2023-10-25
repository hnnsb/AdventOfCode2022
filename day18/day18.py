from aocd.models import Puzzle
from os.path import basename
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
TEST = True
# -----------------------------------------------------
data = puzzle.input_data
if TEST:
    with open(f"day{day}/test.txt", "r") as f:
            data = f.read()
data = data.splitlines()
data = [tuple(map(int,row.split(","))) for row in data]

scan = [[[ False for _ in range(23)] for __ in range(23)] for ___ in range(23)]

for x,y,z in data:
    scan[x][y][z] = True

count = 0
trapped = 0
for x,slice in enumerate(scan):
    for y,row in enumerate(slice):
        for z,cube in enumerate(row):
            dirs = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
            if not cube:
                continue

            for dx,dy,dz in dirs:
                if not scan[x+dx][y+dy][z+dz]:
                    count += 1

print(count)
# puzzle.answer_a = count

# puzzle.answer_b = count
