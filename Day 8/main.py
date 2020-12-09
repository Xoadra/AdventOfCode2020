# 
# 
# 
# Day 8
# Link: https://adventofcode.com/2020/day/8
# 
# 
# 


def import_figures(path):
    figures = []
    with open(path) as file:
        for line in file.readlines():
            operation, magnitude = line.strip().split(" ")
            figures.append((operation, int(magnitude)))
    return figures

def process_instructions(operations, visited=set()):
    accumulator, index = 0, 0
    while index not in visited:
        visited.add(index)
        if index == len(operations):
            return accumulator
        operation, magnitude = operations[index]
        if operation == "acc":
            accumulator += magnitude
            index += 1
        elif operation == "jmp":
            index += magnitude
        elif operation == "nop":
            index += 1
    return accumulator

def remove_infinite_loop(operations):
    for index, (action, value) in enumerate(operations):
        if action != "acc":
            visited, change = set(), "nop" if action == "jmp" else "jmp"
            operations[index] = change, value
            accumulator = process_instructions(operations, visited)
            if len(operations) in visited:
                return accumulator
            operations[index] = action, value
    return -1


operations = import_figures("input.txt")

result_1 = process_instructions(operations) # 1749
result_2 = remove_infinite_loop(operations) # 515

print(result_1, result_2)



