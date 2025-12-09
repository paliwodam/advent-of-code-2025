input_file = "inputs/day4.txt"
with open(input_file) as file:
    diagram = [list(line.strip()) for line in file.readlines()]

n, m = len(diagram), len(diagram[0])

counts = [[0 for _ in range(m)] for _ in range(n)]
adjacents = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]

result = 0

for i in range(n):
    for j in range(m):
        if diagram[i][j] != "@":
            continue
        rolls = -1
        for x, y in adjacents:
            if not (0 <= i+x < n) or not (0 <= j+y < m):
                continue
            if diagram[i+x][j+y] == "@": rolls += 1
        if rolls < 4: result += 1

print(result)