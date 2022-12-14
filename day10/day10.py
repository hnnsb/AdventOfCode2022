from aocd.models import Puzzle
from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
TEST = False
# -----------------------------------------------------
data = puzzle.input_data.splitlines()
if TEST:
    with open(f"day{day}/test.txt", "r") as f:
        data = f.read().splitlines()

w, h = 40, 6
x = 1
xAt40 = []
imp = [20, 60, 100, 140, 180, 220]
sc = ""


def increaseCycle(cycle):
    global sc
    bound = cycle % w
    if x in range(bound-1, bound+2):
        sc += "#"
    else:
        sc += "."
    return cycle + 1


cycle = 0
for line in data:
    if line.startswith("noop"):
        cycle = increaseCycle(cycle)
        if cycle in imp:
            xAt40.append(x)

    if line.startswith("addx"):
        cmd, amt = line.split(" ")
        amt = int(amt)
        cycle = increaseCycle(cycle)
        if cycle in imp:
            xAt40.append(x)
        cycle = increaseCycle(cycle)
        if cycle in imp:
            xAt40.append(x)
        x += amt

res = sum([xAt40[i] * imp[i] for i in range(len(xAt40))])
print(res)
puzzle.answer_a = res

for i, c in enumerate(sc):
    if i % 40 == 0:
        print(sc[i-40:i])
print(sc[i+1-40:i+1])
puzzle.answer_b = "PAPJCBHP"
