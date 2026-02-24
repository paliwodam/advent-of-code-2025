input_file = "inputs/day3.txt"
with open(input_file) as file:
    joltage_ratings = [line.strip() for line in file.readlines()]

def batteries(numeber):
    result = 0
    for joltage_rating in joltage_ratings:
        offset, start, end = 0, 0, len(joltage_rating)
        joltage = ''
        for i in range(numeber-1, -1, -1):
            max_number = max(joltage_rating[start+offset:end-i])
            joltage += max_number
            offset += joltage_rating[start+offset:].index(max_number) + 1
        result += int(joltage)
    return result

def part1():
    return batteries(2)

def part2():
    return batteries(12)

            

    