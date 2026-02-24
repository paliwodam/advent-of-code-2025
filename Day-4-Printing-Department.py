from copy import deepcopy

input_file = "inputs/day4.txt"
with open(input_file) as file:
    diagram = [list(line.strip()) for line in file.readlines()]

n, m = len(diagram), len(diagram[0])

counts = [[0 for _ in range(m)] for _ in range(n)]
adjacents = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]

def accessible_rolls(diagram):
    count = 0
    rolls = []
    for i in range(n):
        for j in range(m):
            if diagram[i][j] != "@":
                continue
            adj_rolls = -1
            for x, y in adjacents:
                if not (0 <= i+x < n) or not (0 <= j+y < m):
                    continue
                if diagram[i+x][j+y] == "@": adj_rolls += 1
            if adj_rolls < 4: 
                rolls.append((i, j))
                count += 1
    return count, rolls

def part1():
    return accessible_rolls(diagram)[0]

def part2():
    result = 0
    updated_diagram = deepcopy(diagram)

    while True:
        count, rolls_to_remove = accessible_rolls(updated_diagram)
        if count == 0: break
        result += count
        for i, j in rolls_to_remove:
            updated_diagram[i][j] = "."
    return result

print(part1())
print(part2())