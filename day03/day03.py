from os.path import basename
from re import findall
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()
import webbrowser
from aocd.models import Puzzle
from aocd import submit
import math


fileName = basename(__file__)
day = int(findall(r"[1-9]+",fileName)[0])
# webbrowser.open(f'https://adventofcode.com/2022/day/{day}', new=1)
# -----------------------------------------------------

puzzle = Puzzle(day=day, year=dotenv_values()["YEAR"])
data = puzzle.input_data.splitlines()
summ = 0
for row in data:
    half = math.floor(len(row)/2)
    first,secon = row[:half],row[half:]
    first,secon = set(first),set(secon)
    common = set.intersection(first,secon).pop()

    if common.isupper():
        priority = ord(common)-ord('A')+27
        summ += priority
    else:
        priority = ord(common)-ord('a')+1
        summ += priority

puzzle.answer_a = summ
sumb = 0
for i in range(0,len(data),3):
    members = [set(data[i]),set(data[i+1]),set(data[i+2])]
    common = set.intersection(*members).pop()
    if common.isupper():
        priority = ord(common)-ord('A')+27
        sumb += priority
    else:
        priority = ord(common)-ord('a')+1
        sumb += priority



puzzle.answer_b = sumb 