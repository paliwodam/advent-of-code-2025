input_file = "inputs/day2.txt"
with open(input_file) as file:
    id_ranges = [r.split('-') for r in file.read().split(',')]

def invalid_ids(part):
    result = []
    for id_range in id_ranges:
        first_id, last_id = id_range
        for id in range (int(first_id), int(last_id)+1):
            id_s = str(id)
            n = len(id_s)
            for i in range(2,n+1):
                if n % i == 0 and id_s[:(n//i)] * i == id_s:
                    result.append(id)
                    break
                if part == 1: break
    return sum(result)

def part1():
    return invalid_ids(1)

def part2():
    return invalid_ids(2)
