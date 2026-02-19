input_file = "inputs/day6.txt"
with open(input_file) as file:
    homework = file.read().splitlines()
    numbers, operators = homework[:-1], homework[-1]
    operators = operators.split()
    numbers = [[int(x) for x in line.split()] for line in numbers]

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

print(total)