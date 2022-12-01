from dotenv import load_dotenv
load_dotenv()
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle

puzzle = Puzzle(day=, year=2022)
data = puzzle.input_data.splitlines()
print(data)

# submit(result))