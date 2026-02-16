input_file = "inputs/day7.txt"
with open(input_file) as file:
    diagram = [line.strip() for line in file.readlines()]

n, m = len(diagram), len(diagram[0])

positions = {(0, diagram[0].index("S"))}
splited = 0

for i in range(n-1):
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


print(splited)