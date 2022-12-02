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
data = puzzle.input_data.splitlines()
data = [(row[0],row[-1]) for row in data]
# A ROck, B Paper, C Scissor  Opponent
scores = {"X":1, "Y":2,"Z":3}
# A = 1   , B = 2, C = 3
# X Rock, Y Paper, Z Scissor  ME
# WIn = 6, Draw = 3, Loose = 0
winning = set(["AY","BZ","CX"])
drawing = set(["AX","BY","CZ"])

sum = 0
for row in data:
    game = row[0] + row[1]
    sum += scores[row[1]]
    if game in winning:
        sum += 6
    elif game in drawing:
        sum += 3

puzzle.answer_a = sum

# X = lose, Y = draw, Z = win
sum = 0
for row in data:
    if row[1] == "X":
        if row[0] == "A":
            sum+= scores["Z"]
        if row[0] == "B":
            sum+= scores["X"]
        if row[0] == "C":
            sum += scores["Y"]

    elif row[1] == "Y":
        sum += 3
        if row[0] == "A":
            sum+= scores["X"]
        if row[0] == "B":
            sum+= scores["Y"]
        if row[0] == "C":
            sum += scores["Z"]
    else:
        sum += 6
        if row[0] == "A":
            sum+= scores["Y"]
        if row[0] == "B":
            sum+= scores["Z"]
        if row[0] == "C":
            sum += scores["X"]


puzzle.answer_b = sum