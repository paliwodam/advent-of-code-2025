input_file = "inputs/day6.txt"
with open(input_file) as file:
    homework = file.read().splitlines()
    numbers, operators = homework[:-1], homework[-1]
    operators = operators.split()
    numbers = [[int(x) for x in line.split()] for line in numbers]

def part1():
    rows, columns = len(numbers), len(operators)
    total = 0
    for i in range(columns):
        result = 1 if operators[i] == "*" else 0
        for j in range(rows):
            if operators[i] == "*": 
                result *= numbers[j][i]
            else:
                result += numbers[j][i]
        total += result
    return total

def part2():
    n, m = len(homework), len(homework[0])
    
    column_start = []
    for idx, c in enumerate(homework[-1]):
        if c == "*" or c == "+": 
            column_start.append(idx)

    total = 0
    for idx, start in enumerate(column_start):
        operator = operators[idx]
        end = m + 1 if idx == len(column_start)-1 else column_start[idx+1]
        result = 1 if operator == "*" else 0
        for j in range(start, end-1):
            number = 0
            for i in range(n-1):
                if homework[i][j] != ' ':
                    number *= 10 
                    number += int(homework[i][j])
            if operator == "*": 
                result *= number
            else:
                result += number
        total += result
    return total
