# 
# 
# 
# Day 11
# Link: https://adventofcode.com/2020/day/11
# 
# 
# 

from copy import deepcopy


def import_figures(path):
    figures = []
    with open(path) as file:
        for line in file.readlines():
            series = [spot for spot in line.strip()]
            figures.append(series)
    return figures

def seats(floor, deep=False):
    seats = {}
    for row in range(len(floor)):
        for column in range(len(floor[row])):
            if floor[row][column] == "L":
                seats[(row, column)] = set()
                for vertical, horizontal in offsets(row, column):
                    level, index = row + vertical, column + horizontal
                    while deep and valid(floor, level, index, "."):
                        level, index = level + vertical, index + horizontal
                    if valid(floor, level, index, "L"):
                        seats[(row, column)].add((level, index))
    return seats

def offsets(row, column):
    for vertical in range(-1, 2):
        for horizontal in range(-1, 2):
            if vertical != 0 or horizontal != 0:
                yield vertical, horizontal

def valid(floor, row, column, target):
    is_minimal = row >= 0 and column >= 0
    is_maximal = row < len(floor) and column < len(floor[row])
    return is_minimal and is_maximal and floor[row][column] == target

def count_seated(floor, seats):
    quantity = 0
    for vertical, horizontal in seats:
        if floor[vertical][horizontal] == "#":
            quantity += 1
    return quantity

def seats_occupied(floor, seats, unset):
    updates, occupied = 0, 0
    current, previous = deepcopy(floor), None
    while previous is None or updates != 0:
        updates, occupied, previous = 0, 0, deepcopy(current)
        for (row, column), neighbors in seats.items():
            adjacencies = count_seated(previous, neighbors)
            if previous[row][column] == "L" and adjacencies == 0:
                current[row][column] = "#"
                updates += 1
            if previous[row][column] == "#" and adjacencies >= unset:
                current[row][column] = "L"
                updates += 1
            if current[row][column] == "#":
                occupied += 1
    return occupied


floor = import_figures("input.txt")

result_1 = seats_occupied(floor, seats(floor), 4) # 2265
result_2 = seats_occupied(floor, seats(floor, True), 5) # 2045

print(result_1, result_2)



