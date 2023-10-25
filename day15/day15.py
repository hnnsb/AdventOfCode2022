from aocd.models import Puzzle
from os.path import basename
from dotenv import load_dotenv
from dotenv import dotenv_values
from re import findall
load_dotenv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
TEST = False
# -----------------------------------------------------
data = puzzle.input_data
if TEST:
    with open(f"day{day}/test.txt", "r") as f:
        data = f.read()
    row = 10
else:
    row = 2_000_000
data = data.splitlines()
N = len(data)
sensors = []
beacons = []
minX, minY, maxX, maxY = int(1e10), int(1e10), 0, 0

for line in data:
    sx, sy, bx, by = list(map(int,findall(r"\d+", line)))
    minX, minY = min(minX, sx, bx), min(minY, sy, by)
    maxX, maxY = max(maxX, sx, bx), max(maxY, sy, by)
    sensors.append((sx, sy))
    beacons.append((bx, by))

print(minX,maxX,minY,maxY)
possibleX = set(range(-int(1e7),int(1e7)))
initialLegth = len(possibleX)
beaconsInRow = set()
for i in range(N):
    print(i,"/",N)
    sx,sy = sensors[i]
    bx,by = beacons[i]

    if by == row:
        beaconsInRow.add(bx)
    dist = abs(sx-bx) + abs(sy-by)
    toRemove = []
    #-------- SLow
    for x in possibleX:
        dx = abs(x-sx) + abs(row-sy)
        if  dx <= dist:
            toRemove.append(x)
    #---------------
    for x in toRemove:
        possibleX.remove(x)


for b in beaconsInRow:
    possibleX.add(b)

res = initialLegth - len(possibleX)
print(res)

# puzzle.answer_a = count
# puzzle.answer_b =
