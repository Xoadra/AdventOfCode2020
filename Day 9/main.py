# 
# 
# 
# Day 9
# Link: https://adventofcode.com/2020/day/9
# 
# 
# 


def import_figures(path):
    figures = []
    with open(path) as file:
        for line in file.readlines():
            figures.append(int(line.strip()))
    return figures

def first_non_sum(numbers):
    preamble = {numbers[index] for index in range(25)}
    for index in range(25, len(numbers)):
        issum = False
        for number in preamble:
            if numbers[index] - number in preamble:
                issum = True
        if not issum:
            return numbers[index]
        preamble.remove(numbers[index - 25])
        preamble.add(numbers[index])
    return -1

def contiguous_two_sum(numbers, target):
    total, lowest, highest = numbers[0] + numbers[1], 0, 1
    while total != target and highest < len(numbers) - 1:
        if total < target:
            highest += 1
            total += numbers[highest]
        elif total > target:
            total -= numbers[lowest]
            lowest += 1
    minimum, maximum = float("inf"), float("-inf")
    for index in range(lowest, highest + 1):
        minimum = min(minimum, numbers[index])
        maximum = max(maximum, numbers[index])
    return maximum + minimum


numbers = import_figures("input.txt")

result_1 = first_non_sum(numbers) # 23278925
result_2 = contiguous_two_sum(numbers, result_1) # 4011064

print(result_1, result_2)



