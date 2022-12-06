from aocd.models import Puzzle
from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()


fileName = basename(__file__)
day = int(findall(r"[1-9]+", fileName)[0])
# -----------------------------------------------------

puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
data = puzzle.input_data
for i, c in enumerate(data):
    s, e = i, i+4

    if e > len(data):
        break
    marker = set(data[s:e])
    if len(marker) == 4:
        print(e)
        break

puzzle.answer_a = e

for i, c in enumerate(data):
    s, e = i, i+14

    if e > len(data):
        break
    marker = set(data[s:e])
    if len(marker) == 14:
        print(e)
        break

puzzle.answer_b = e
