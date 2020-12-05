# 
# 
# 
# Day 5
# Link: https://adventofcode.com/2020/day/5
# 
# 
# 

import math


def import_figures(path):
    figures = []
    with open(path) as file:
        for line in file.readlines():
            figures.append(line.strip())
    return figures

def get_seats(directions):
    seats = []
    for direction in directions:
        lower, upper = 0, 127
        for index in range(7):
            if direction[index] == "F":
                upper = math.floor((upper + lower) / 2)
            elif direction[index] == "B":
                lower = math.ceil((upper + lower) / 2)
        row = lower if direction[6] == "F" else upper
        lower, upper = 0, 7
        for index in range(7, 10):
            if direction[index] == "L":
                upper = math.floor((upper + lower) / 2)
            elif direction[index] == "R":
                lower = math.ceil((upper + lower) / 2)
        column = lower if direction[9] == "L" else upper
        seats.append((row * 8) + column)
    return seats

def find_seat(seats):
    occupied = set(seats)
    lower, upper = min(seats), max(seats)
    for seat in range(lower + 1, upper):
        if seat not in occupied:
            return seat
    return -1


seats = get_seats(import_figures("input.txt"))

result_1 = max(seats) # 806
result_2 = find_seat(seats) # 562

print(result_1, result_2)



