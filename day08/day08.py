from aocd.models import Puzzle
from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()

fileName = basename(__file__)
day = int(findall(r"[1-9]+", fileName)[0])
puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
TEST = False
# -----------------------------------------------------
data =  puzzle.input_data.splitlines()
if TEST:
    with open("day08/test.txt", "r") as f:
        data = f.read().splitlines()
data = [list(map(int,row.strip())) for row in data]
w, h = len(data[1]),len(data)
visible = [[True for _ in range(w)] for __ in range(h)]
countVisible = 0

def isTreeVisible(x,y):
    t = data[y][x]
    topBigger = False
    botBigger = False
    for dy in range(h):
        if topBigger and botBigger:
            break
        if data[dy][x] >= t:
            if dy < y:
                topBigger = True
            if dy > y:
                botBigger = True
    rightBigger = False
    leftBigger = False          
    for dx in range(w):
        if rightBigger and leftBigger:
            break
        if data[y][dx] >= t:
            if dx < x:
                rightBigger = True
            if dx > x:
                leftBigger = True
    return not topBigger or not botBigger or not rightBigger or not leftBigger

for y,row in enumerate(data):
    for x,t in enumerate(row):
        if not visible[y][x]:
            continue
        if x == 0 or y == 0 or x == w-1 or y == h-1:
            visible[y][x] = True
            continue
        visible[y][x] = isTreeVisible(x,y)



for row in visible:
    for b in row:
        if b: countVisible += 1
puzzle.answer_a =1803


def lookDir(x,y,dir):
    if dir == "UP":
        dy = 1
        while y-dy >= 0:
            if data[y-dy][x] >= data[y][x]:
                return dy
            dy+=1
        return dy-1
    if dir == "DOWN":
        dy = 1
        while y+dy < h:
            if data[y+dy][x] >= data[y][x]:
                return dy
            dy+=1
        return dy-1
    if dir == "LEFT":
        dx = 1
        while x-dx >= 0:
            if data[y][x-dx] >= data[y][x]:
                return dx
            dx += 1
        return dx-1
    if dir == "RIGHT":
        dx = 1
        while x+dx < w:
            if data[y][x+dx] >= data[y][x]:
                return dx
            dx += 1
        return dx-1
            
scenic= [[0 for _ in range(w)] for __ in range(h)]
for y,row in enumerate(data):
    for x,t in enumerate(row):
        score = 0
        score = lookDir(x,y,"UP")*lookDir(x,y,"DOWN")*lookDir(x,y,"LEFT")*lookDir(x,y,"RIGHT")

        scenic[y][x] = score
res = max(map(max,scenic))

puzzle.answer_b = res
