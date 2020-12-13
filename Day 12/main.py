# 
# 
# 
# Day 12
# Link: https://adventofcode.com/2020/day/12
# 
# 
# 

import re


def import_figures(path):
    figures, splitter = [], re.compile(r"(?<=\D)")
    with open(path) as file:
        for line in file.readlines():
            direction, magnitude = splitter.split(line.strip())
            figures.append((direction, int(magnitude)))
    return figures

def pivot_face(orientation, direction, magnitude):
    offsets = {"N": 0, "E": 90, "S": 180, "W": 270}
    degrees = {0: "N", 90: "E", 180: "S", 270: "W"}
    rotation = magnitude * (-1 if direction == "L" else 1)
    position = (offsets[orientation] + rotation) % 360
    return degrees.get(position, None)

def distance_traveled_1(directions):
    orientation, vertical, horizontal = "E", 0, 0
    for direction, magnitude in directions:
        if direction == "F":
            distance = magnitude * (-1 if orientation in "SW" else 1)
            vertical += distance if orientation in "NS" else 0
            horizontal += distance if orientation in "EW" else 0
        elif direction in "NSEW":
            distance = magnitude * (-1 if direction in "SW" else 1)
            vertical += distance if direction in "NS" else 0
            horizontal += distance if direction in "EW" else 0
        elif direction in "LR":
            orientation = pivot_face(orientation, direction, magnitude)
    return abs(vertical) + abs(horizontal)

def distance_traveled_2(directions, latitude, longitude):
    vertical, horizontal = 0, 0
    for direction, magnitude in directions:
        if direction == "F":
            vertical += magnitude * latitude
            horizontal += magnitude * longitude
        elif direction in "NSEW":
            distance = magnitude * (-1 if direction in "SW" else 1)
            latitude += distance if direction in "NS" else 0
            longitude += distance if direction in "EW" else 0
        elif direction in "LR":
            rotation = magnitude * (-1 if direction == "L" else 1)
            if rotation % 360 == 90:
                latitude, longitude = -longitude, latitude
            if rotation % 360 == 180:
                latitude, longitude = -latitude, -longitude
            if rotation % 360 == 270:
                latitude, longitude = longitude, -latitude
    return abs(vertical) + abs(horizontal)


directions = import_figures("input.txt")

result_1 = distance_traveled_1(directions) # 1177
result_2 = distance_traveled_2(directions, 1, 10) # 46530

print(result_1, result_2)


