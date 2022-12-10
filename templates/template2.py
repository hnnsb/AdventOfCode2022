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
print(data)

# puzzle.answer_a =
# puzzle.answer_b =
