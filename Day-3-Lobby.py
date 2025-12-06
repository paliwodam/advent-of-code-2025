input_file = "inputs/day3.txt"
with open(input_file) as file:
    joltage_ratings = [line.strip() for line in file.readlines()]

result = 0
for joltage_rating in joltage_ratings:
    n = len(joltage_rating)
    max_number = max(joltage_rating[:n-1])
    max_index = joltage_rating.index(max_number)
    second_max_number = max(joltage_rating[max_index+1:])
    result += int(max_number+second_max_number)

print(result)