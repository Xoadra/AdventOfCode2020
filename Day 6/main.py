# 
# 
# 
# Day 6
# Link: https://adventofcode.com/2020/day/6
# 
# 
# 


def import_figures(path):
    figures, members, group = [], 0, {}
    with open(path) as file:
        for line in file.readlines():
            if line.isspace():
                figures.append((members, group))
                members, group = 0, {}
            else:
                for question in line.strip():
                    group[question] = group.get(question, 0) + 1
                members += 1
    figures.append((members, group))
    return figures

def everyone_answered(responses):
    quantity = 0
    for members, response in responses:
        for question, yeses in response.items():
            if yeses == members:
                quantity += 1
    return quantity


responses = import_figures("input.txt")

result_1 = sum([len(group) for members, group in responses]) # 6735
result_2 = everyone_answered(responses) # 3221

print(result_1, result_2)


