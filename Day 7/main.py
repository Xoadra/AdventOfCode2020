# 
# 
# 
# Day 7
# Link: https://adventofcode.com/2020/day/7
# 
# 
# 

import re
from queue import Queue


def import_figures(path):
    figures, decoupler = [], re.compile(r"(?<=\d)\s")
    splitter = re.compile(r"\sbags contain\s|no other bags\.?|\sbags?,?\s?\.?")
    with open(path) as file:
        for line in file.readlines():
            relations = splitter.split(line.strip())
            color, *options = [phrase for phrase in relations if phrase != ""]
            bags = [tuple(decoupler.split(phrase)) for phrase in options]
            figures.append((color, bags))
    return figures

def build_graph(relations):
    graph = {}
    for color, edges in relations:
        graph[color] = graph.get(color, {})
        for volume, pigment in edges:
            graph[pigment] = graph.get(pigment, {})
            graph[color][pigment] = int(volume)
    return graph

def colors_containing(target, colors):
    queue, visited = Queue(), set()
    for color, edges in colors.items():
        if target in edges:
            queue.put(color)
    while not queue.empty():
        size = queue.qsize()
        for step in range(size):
            color = queue.get()
            visited.add(color)
            for pigment, edges in colors.items():
                if pigment != target and color in edges:
                    queue.put(pigment)
    return len(visited)

def colors_within(target, colors):
    quantity = 0
    for color, amount in colors[target].items():
        quantity += amount + amount * colors_within(color, colors)
    return quantity


relations = import_figures("input.txt")
colors = build_graph(relations)

output_1 = colors_containing("shiny gold", colors) # 103
output_2 = colors_within("shiny gold", colors) # 1469

print(output_1, output_2)



