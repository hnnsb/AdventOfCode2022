from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()
from aocd.models import Puzzle


fileName = basename(__file__)
day = int(findall(r"[1-9]+",fileName)[0])
# -----------------------------------------------------

puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
crates,steps = puzzle.input_data.split("\n\n")
crates = [["empty"],
    ["D","H","R","Z","S","P","W","Q"],
    ["F","H","Q","W","R","B","V"],
    ["H","S","V","C"],
    ["G","F","H"],
    ["Z","B","J","G","P"],
    ["L","F","W","H","J","T","Q"],
    ["N","J","V","L","D","W","T","Z"],
    ["F","H","G","J","C","Z","T","D"],
    ["H","B","M","V","P","W"]
]

# crates = [["empty"],["N","Z"],["D","C","M"],["P"]]
# steps = 'move 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2'

steps = [row.replace("move ","") for row in steps.splitlines()]
steps = [row.split(" from ") for row in steps]
for step in steps:
    for i in range(int(step[0])):
        f = int(step[1][0])
        t = int(step[1][-1])
        popped = crates[f].pop(0)
        crates[t].insert(0,popped)
res = ""
for crate in crates:
    if crate[0] == "empty":
        continue
    res += crate[0]
print(res)
puzzle.answer_a = res

crates = [["empty"],
    ["D","H","R","Z","S","P","W","Q"],
    ["F","H","Q","W","R","B","V"],
    ["H","S","V","C"],
    ["G","F","H"],
    ["Z","B","J","G","P"],
    ["L","F","W","H","J","T","Q"],
    ["N","J","V","L","D","W","T","Z"],
    ["F","H","G","J","C","Z","T","D"],
    ["H","B","M","V","P","W"]
]

for step in steps:
    f = int(step[1][0])
    t = int(step[1][-1])
    for i in range(int(step[0]),0,-1):
        popped = crates[f].pop(i-1)
        crates[t].insert(0,popped)
res = ""
for crate in crates:
    if crate[0] == "empty":
        continue
    res += crate[0]
print(res)
puzzle.answer_b = res