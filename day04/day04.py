from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()
import webbrowser
from aocd.models import Puzzle
from aocd import submit


fileName = basename(__file__)
day = int(findall(r"[1-9]+",fileName)[0])
# webbrowser.open(f'https://adventofcode.com/2022/day/{day}', new=1)
# -----------------------------------------------------

puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
data = puzzle.input_data.splitlines()
data = [row.split(",") for row in data]
data = [[col.split("-") for col  in row] for row in data]
data = [[[int(i) for i in col]for col in row] for row in data]

count = 0
for row in data:
    if (row[0][0] <= row[1][0] and row[0][1] >= row[1][1]) or (row[0][0] >= row[1][0] and row[0][1] <= row[1][1]):
        count += 1

puzzle.answer_a = count

count = 0
for row in data:
    if (row[0][0] >= row[1][0] and row[0][0] <= row[1][1]) or (row[0][1] >= row[1][0] and row[0][1] <= row[1][1]):
        count += 1
    elif (row[1][0] >= row[0][0] and row[1][0] <= row[0][1]) or (row[1][1] >= row[0][0] and row[1][1] <= row[0][1]):
        count += 1
puzzle.answer_b = count