input_file = "inputs/day2.txt"
with open(input_file) as file:
    id_ranges = [r.split('-') for r in file.read().split(',')]

result = []
for id_range in id_ranges:
    first_id, last_id = id_range
    for id in range (int(first_id), int(last_id)+1):
        id_s = str(id)
        n = len(id_s) // 2
        if id_s[:n] == id_s[n:]:
            result.append(id)

print(sum(result))

