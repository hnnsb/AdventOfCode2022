from aocd.models import Puzzle
from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
import math
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
    operations = [
        lambda x: x * 19,
        lambda x: x + 6,
        lambda x: x * x,
        lambda x: x + 3,
    ]
    
else:
    operations = [
        lambda x: x * 7,
        lambda x: x + 4,
        lambda x: x + 2,
        lambda x: x + 7,
        lambda x: x * 17,
        lambda x: x + 8,
        lambda x: x + 6,
        lambda x: x * x,
    ]

data = [monkey.split("\n") for monkey in data]
monkeys = []
for i, m in enumerate(data):
    monkey = {}
    items = m[1].split(": ")[1].split(", ")
    monkey["items"] = [int(item) for item in items]
    monkey["test"] = int(m[3].split(" ")[-1])
    monkey[True] = int(m[4].split(" ")[-1])
    monkey[False] = int(m[5].split(" ")[-1])
    monkey["inspected"] = 0
    monkeys.append(monkey)

product = 2*3*5*7*11*13*17*19
part1 = False
if part1:
    limit = 20
else:
    limit = 10000
for round in range(limit):
    for i, monkey in enumerate(monkeys):
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            monkey["inspected"] += 1
            worrylevel = operations[i](item) % product
            if part1:
                worrylevel = worrylevel // 3
            test = worrylevel % monkey["test"] == 0

            monkeys[monkey[test]]["items"].append(worrylevel)

maxInspec = []
for monkey in monkeys:
    maxInspec.append(monkey["inspected"])
maxInspec = sorted(maxInspec)
print(maxInspec)
print(maxInspec[-1] * maxInspec[-2])
if part1:
    puzzle.answer_a = maxInspec[-1] * maxInspec[-2]
else:
    puzzle.answer_b = maxInspec[-1] * maxInspec[-2]
