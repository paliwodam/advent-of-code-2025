from collections import defaultdict

input_file = "inputs/day11.txt"

conneced_by = defaultdict(list)

end = "out"

with open(input_file) as file:
    for line in file.readlines():
        from_device, *to_devices = line.split()
        for d in to_devices: 
            conneced_by[d].append(from_device[:-1])

def part1():
    paths_to = {'you': 1}

    def recur(device):
        if device in paths_to:
            return paths_to[device]
        paths_to[device] = sum(recur(d) for d in conneced_by[device])
        return paths_to[device]
    return recur(end)

def part2():
    paths_to = {
        ('svr', True, True): 1, 
        ('svr', True, False): 0, 
        ('svr', False, True): 0, 
        ('svr', True, False): 0
        }

    def recur(device, fft, dac):
        if device == 'fft': fft = True
        if device == 'dac': dac = True
        
        if (device, fft, dac) in paths_to:
            return paths_to[(device, fft, dac)]
        paths_to[(device, fft, dac)] = sum(recur(d, fft, dac) for d in conneced_by[device])
        return paths_to[(device, fft, dac)]
    
    return recur(end, False, False)

print(part2())
