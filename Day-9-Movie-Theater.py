input_file = "inputs/day9.txt"
with open(input_file) as file:
    coords = [line.split(",") for line in file.readlines()]
    coords = [(int(x[0]), int(x[1])) for x in coords]
    
largest_area = 0

for i, j in coords:
    for k, l in coords:
        area = (abs(k-i)+1) * (abs(l-j)+1)
        largest_area = max(area, largest_area)

print(largest_area)