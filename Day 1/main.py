# 
# 
# 
# Day 1
# Link: https://adventofcode.com/2020/day/1
# 
# 
# 


def import_figures(path):
    figures = []
    with open(path) as file:
        for line in file.readlines():
            figures.append(int(line))
    return figures

def multiply_two_sum(values, target):
    visited = set()
    for value in values:
        complement = target - value
        if complement in visited:
            return value * complement
        visited.add(value)

def multiply_three_sum(values, target):
    visited = {values[0]}
    for outer in range(len(values)):
        for inner in range(outer + 1, len(values)):
            aggregate = values[outer] + values[inner]
            complement = target - aggregate
            if complement in visited:
                return values[outer] * values[inner] * complement
            visited.add(values[inner])


numbers = import_figures("input.txt")

result_1 = multiply_two_sum(numbers, 2020) # 55776
result_2 = multiply_three_sum(numbers, 2020) # 223162626

print(result_1, result_2)



