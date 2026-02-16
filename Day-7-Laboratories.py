from collections import defaultdict
input_file = "inputs/day7.txt"
with open(input_file) as file:
    diagram = [line.strip() for line in file.readlines()]

n, m = len(diagram), len(diagram[0])

def part1():
    positions = {(0, diagram[0].index("S"))}
    splited = 0

    for _ in range(n-1):
        new_positions = set()
        for position in positions:
            x, y = position
            if diagram[x+1][y] == "^":
                new_positions.add((x+1, y-1))
                new_positions.add((x+1, y+1))
                splited += 1
            else:
                new_positions.add((x+1, y))
        positions = new_positions

    return splited

def part2():
    positions = {(0, diagram[0].index("S")): 1}
    
    for _ in range(n-1):
        new_positions = defaultdict(int)
        for position, timelines in positions.items():
            x, y = position
            if diagram[x+1][y] == "^":
                new_positions[(x+1, y-1)] += timelines
                new_positions[(x+1, y+1)] += timelines
            else:
                new_positions[(x+1, y)] += timelines
        positions = new_positions

    return sum(positions.values())
