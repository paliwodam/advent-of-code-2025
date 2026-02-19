import re

input_file = "inputs/day10.txt"
with open(input_file) as file:
    manual = []
    for line in file.readlines():
        lights = re.search(r'\[.*\]', line).group().strip("[]")
        joltages = [int(x) for x in re.search(r'\{.*\}', line).group().strip("{}").split(",")]
        buttons = re.search(r'\].*\{', line).group().strip("] {").split()
        for i in range(len(buttons)):
            button = buttons[i].strip("()")
            button = tuple(int(x) for x in button.split(","))
            buttons[i] = button
        manual.append((lights, buttons, joltages))

def presses(lights, buttons):
    start = ['.'] * len(lights)
    visited = {tuple(start): True}
    bfs = [(1, start)]
    while bfs:
        count, old_state = bfs.pop(0)
        for button in buttons:
            state = list(old_state)
            for idx in button:
                state[idx] = "." if state[idx] == "#" else "#"
            if ''.join(state) == lights:
                return count
            if tuple(state) not in visited:
                visited[tuple(state)] = True
                bfs.append((count+1, state))

def part1():
    return sum([presses(lights, buttons) for lights, buttons, _ in manual])

print(part1())