# 
# 
# 
# Day 10
# Link: https://adventofcode.com/2020/day/10
# 
# 
# 


def import_figures(path):
    figures = []
    with open(path) as file:
        for line in file.readlines():
            figures.append(int(line.strip()))
    return figures

def jolt_differences(jolts):
    jolts.sort()
    onesets, threesets = 1, 1
    for index in range(len(jolts)):
        if jolts[index] - 1 == jolts[index - 1]:
            onesets += 1
        elif jolts[index] - 3 == jolts[index - 1]:
            threesets += 1
    return onesets * threesets

def jolt_differences(jolts):
    onesets, threesets = 1, 1
    adapters, initial = set(), float("inf")
    for jolt in jolts:
        adapters.add(jolt)
        initial = min(jolt, initial)
    while len(adapters) > 1:
        if initial + 1 in adapters:
            adapters.remove(initial)
            onesets, initial = onesets + 1, initial + 1
        elif initial + 3 in adapters:
            adapters.remove(initial)
            threesets, initial = threesets + 1, initial + 3
    return onesets * threesets

def combine_adapters(value, target, adapters, visited={}):
    if value == target:
        return 1
    combinations = 0
    for offset in range(1, 4):
        if value + offset in adapters:
            if value + offset not in visited:
                ways = combine_adapters(value + offset, target, adapters, visited)
                visited[value + offset] = ways
            combinations += visited[value + offset]
    return combinations

def adapter_combinations(jolts):
    adapters, target = set(), float("-inf")
    for jolt in jolts:
        adapters.add(jolt)
        target = max(jolt, target)
    return combine_adapters(0, target, adapters)


jolts = import_figures("input.txt")

result_1 = jolt_differences(jolts) # 1848
result_2 = adapter_combinations(jolts) # 8099130339328

print(result_1, result_2)



