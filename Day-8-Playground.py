from math import prod
import time

input_file = "inputs/day8.txt"
with open(input_file) as file:
    positions = [line.split(",") for line in file.readlines()]

distances = []

n = len(positions)

for i in range(n-1):
    for j in range(i+1, n):
        x1, y1, z1 = positions[i]
        x2, y2, z2 = positions[j]
        x1, y1, z1 = int(x1), int(y1), int(z1)
        x2, y2, z2 = int(x2), int(y2), int(z2)
        distance = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2)
        distances.append((distance, i, j))

distances.sort()

class UnionFind: 
    def __init__(self, size):
        self.parent = list(range(size))
        self.sizes = [1 for _ in range(size)]

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        self.parent[irep] = jrep

        tmp = self.sizes[irep]
        self.sizes[jrep] += tmp
        self.sizes[irep] -= tmp
    
uf = UnionFind(n)

def part1():
    cnt = 0
    while cnt < 1000:
        _, i, j = distances.pop(0)
        uf.unite(i, j)
        cnt += 1

    return prod(sorted(uf.sizes, reverse=True)[:3])


def part2():
    while True:
        _, i, j = distances.pop(0)
        uf.unite(i, j)
        if uf.sizes[uf.find(j)] == n:
            return int(positions[i][0]) * int(positions[j][0])
