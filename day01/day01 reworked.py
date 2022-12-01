from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()
from aocd.models import Puzzle
from aocd import submit

fileName = basename(__file__)
day = int(findall(r"[1-9]+",fileName)[0])
puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
# -----------------------------------------------------
data = puzzle.input_data.splitlines()
sums = []
s = 0
for c in data:
    if c == "":
        sums.append(s)
        s = 0
    else:
        s += int(c)    

print("Part 1: ", max(sums))
print("Part 2: ", sum(sorted(sums)[-3:]))
