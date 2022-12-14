from aocd.models import Puzzle
from os.path import basename
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
TEST = False
# -------- Importing Data --------
data = puzzle.input_data
if TEST:
    with open(f"day{day}/test.txt", "r") as f:
        data = f.read()
# --------------------------------
data = [row.split(" -> ") for row in data.splitlines()]
data = [[(int(coor.split(",")[0]), int(coor.split(",")[1]))
         for coor in row] for row in data]


def prettyPrint(rock: set, sand: set, minX: int, maxX: int, height: int, name: str):
    res: str = ""
    for y in range(0, height+1):
        line: str = ""
        for x in range(minX, maxX+1):
            if (x, y) in rock:
                if (x, y) in sand:
                    line += "."
                else:
                    line += "#"
            else:
                line += " "
        res += line + "\n"
    with open(f"day{day}/result {name}.txt", "w") as f:
        f.write(res)


minX, minY, maxX, maxY = int(1e10), int(1e10), 0, 0
rock = set()  # Keep track of coordinates of solids: rocks, resting sand.
for row in data:
    for i in range(len(row)-1):
        start, end = row[i], row[i+1]
        diffX, diffY = end[0]-start[0], end[1]-start[1]
        stepX, stepY = 0, 0
        if abs(diffX) > 0:
            stepX = 1 if diffX > 0 else -1
        if abs(diffY) > 0:
            stepY = 1 if diffY > 0 else -1
        cur = start
        rock.add(tuple(cur))
        minX = min(minX, start[0], end[0])
        minY = min(minY, start[1], end[1])
        maxX = max(maxX, start[0], end[0])
        maxY = max(maxY, start[1], end[1])
        while cur != end:
            cur = cur[0]+stepX, cur[1]+stepY
            rock.add(tuple(cur))


rockB = rock.copy()

sandStart = (500, 0)
sand = set()  # Keep track of sand, only for pretty output
count = 0
fallingForever = False
while not fallingForever:
    unit = sandStart
    while unit not in rock:
        sand.add(unit)
        below = unit[0], unit[1]+1
        left = unit[0]-1, unit[1]+1
        right = unit[0]+1, unit[1]+1
        if below not in rock:
            unit = below
        elif left not in rock:
            unit = left
        elif right not in rock:
            unit = right
        else:
            # Resting sand unit counts as solid for next falling unit
            rock.add(unit)

        if (unit[1] > maxY):
            fallingForever = True
            break

    count += 1

count -= 1  # Adjust for last sand unit falling forever
prettyPrint(rock, sand, minX, maxX, maxY+2, "part1")
print(count)
puzzle.answer_a = count

# -------- Part 2 -------- #
sandStart = (500, 0)
sand = set()
count = 0
blocked = False

for x in range(minX-500, maxX+500):
    rockB.add((x, maxY+2))

while not blocked:
    unit = sandStart
    while unit not in rockB:
        sand.add(unit)
        below = unit[0], unit[1]+1
        left = unit[0]-1, unit[1]+1
        right = unit[0]+1, unit[1]+1
        if below not in rockB:
            unit = below
        elif left not in rockB:
            unit = left
        elif right not in rockB:
            unit = right
        else:
            rockB.add(unit)

        if (unit == sandStart):
            blocked = True
            break
    count += 1

prettyPrint(rockB, sand, 500-(maxY+2), 500+maxY+2, maxY+2, "part2")

print(count)
puzzle.answer_b = count
