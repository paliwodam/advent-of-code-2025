input_file = "inputs/day1.txt"
with open(input_file) as file:
    rotations = [line.strip() for line in file.readlines()]

starting_position = 50


def part1():
    position = starting_position
    zero_count = 0
    for rotation in rotations:
        direction = rotation[0]
        clicks = int(rotation[1:])
        
        if direction == 'L':
            position = (position-clicks) % 100
        if direction == 'R':
            position = (position+clicks) % 100
        if position == 0: zero_count+=1

    return zero_count


def part2():
    position = starting_position
    zero_count = 0
    for rotation in rotations:
        direction = rotation[0]
        clicks = int(rotation[1:])
        for _ in range(clicks):
            if direction == 'L':
                position -= 1
            if direction == 'R':
                position += 1
            if position % 100 == 0:
                zero_count += 1
    return zero_count

print(part1())
print(part2())