with open("day01/input.txt", "r") as f:
    data = []
    sub = []
    for row in f:
        if row == '\n':
            data.append(sub)
            sub = []
        else:
            sub.append(int(row.strip('\n')))

sums =  [sum(food) for food in data]
print("Part 1: ", max(sums))
print("Part 2: ", sum(sorted(sums)[-3:]))
