from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()
from aocd.models import Puzzle
from aocd import submit

fileName = basename(__file__)
day = int(findall(r"[1-9]+",fileName)[0])
# -----------------------------------------------------

puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
data = puzzle.input_data
print(data)

# puzzle.answer_a = 
# puzzle.answer_b = 