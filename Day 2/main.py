# 
# 
# 
# Day 2
# Link: https://adventofcode.com/2020/day/2
# 
# 
# 

import re


def import_figures(path):
    figures = []
    with open(path) as file:
        for line in file.readlines():
            lower, upper, symbol, password = re.findall(r"\w+", line)
            figures.append((int(lower), int(upper), symbol, password))
    return figures

def valid_passwords_1(criteria):
    quantity = 0
    for lower, upper, symbol, password in criteria:
        frequency = sum([1 for character in password if character == symbol])
        quantity += 1 if frequency >= lower and frequency <= upper else 0
    return quantity

def valid_passwords_2(criteria):
    quantity = 0
    for lower, upper, symbol, password in criteria:
        if upper <= len(password):
            first = 1 if password[lower - 1] == symbol else 0
            second = 1 if password[upper - 1] == symbol else 0
            quantity += 1 if first + second == 1 else 0
    return quantity


figures = import_figures("input.txt")

result_1 = valid_passwords_1(figures) # 524
result_2 = valid_passwords_2(figures) # 485

print(result_1, result_2)


