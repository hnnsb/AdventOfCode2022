from copy import deepcopy
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
data = puzzle.input_data.split("\n\n")
if TEST:
    with open(f"day{day}/test.txt", "r") as f:
        data = f.read().split("\n\n")

data = [monkey.split("\n") for monkey in data]
monkeys = []
for i, m in enumerate(data):
    monkey = {}
    items = m[1].split(": ")[1].split(", ")
    monkey["items"] = [int(item) for item in items]
    operation = " ".join(m[2].split(" ")[-3:])
    monkey["operation"] = lambda old, operation=operation: eval(operation)
    monkey["test"] = int(m[3].split(" ")[-1])
    monkey[True] = int(m[4].split(" ")[-1])
    monkey[False] = int(m[5].split(" ")[-1])
    monkey["inspected"] = 0
    monkeys.append(monkey)

monkeys2 = deepcopy(monkeys)

for round in range(20):
    for i, monkey in enumerate(monkeys):
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            monkey["inspected"] += 1
            worrylevel = monkey["operation"](item) // 3
            test = worrylevel % monkey["test"] == 0
            monkeys[monkey[test]]["items"].append(worrylevel)

maxInspec = []
for monkey in monkeys:
    maxInspec.append(monkey["inspected"])
maxInspec = sorted(maxInspec)
print("Part 1: ", maxInspec[-1] * maxInspec[-2])
puzzle.answer_a = maxInspec[-1] * maxInspec[-2]


# Part 2
commonMultiple = 1
for monkey in monkeys:
    commonMultiple *= monkey["test"]

for round in range(10000):
    for i, monkey in enumerate(monkeys2):
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop(0)
            monkey["inspected"] += 1
            worrylevel = monkey["operation"](item) % commonMultiple
            test = worrylevel % monkey["test"] == 0
            monkeys2[monkey[test]]["items"].append(worrylevel)

maxInspec = []
for monkey in monkeys2:
    maxInspec.append(monkey["inspected"])
maxInspec = sorted(maxInspec)
print("Part 2: ", maxInspec[-1] * maxInspec[-2])
puzzle.answer_b = maxInspec[-1] * maxInspec[-2]
