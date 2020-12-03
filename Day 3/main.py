# 
# 
# 
# Day 3
# Link: https://adventofcode.com/2020/day/3
# 
# 
# 


def import_figures(path):
    chart = []
    with open(path) as file:
        for line in file.readlines():
            chart.append(line.strip())
    return chart

def count_trees(grid, down, right):
    trees, row, column = 0, down, right
    while row < len(grid):
        if column >= len(grid[row]):
            column = column % len(grid[row])
        if grid[row][column] == "#":
            trees += 1
        row, column = row + down, column + right
    return trees

def multiply_trees(grid, slopes):
    product = 1
    for slope in slopes:
        product *= count_trees(grid, *slope)
    return product


grid = import_figures("input.txt")
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

result_1 = count_trees(grid, *slopes[1]) # 270
result_2 = multiply_trees(grid, slopes) # 2122848000

print(result_1, result_2)


