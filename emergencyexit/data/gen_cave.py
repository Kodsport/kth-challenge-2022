#!/usr/bin/env python3

import sys
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))
n = int(cmdlinearg('n', 10))
m = int(cmdlinearg('m', 10))
k = int(cmdlinearg('k', 10))
empty = int(cmdlinearg('empty', 10))
branches = int(cmdlinearg('branches', 1))

DX = [0,0,-1,1]
DY = [1,-1,0,0]
cells = []
edge_cells = []
grid = []
for i in range(0,n):
    row = ['#'] * m
    grid.append(row)
    for j in range(0,m):
        if i == 0 or j == 0 or i == n-1 or j == m-1:
            edge_cells.append((i, j))
        else:
            cells.append((i, j))
random.shuffle(edge_cells)
grid[edge_cells[0][0]][edge_cells[0][1]] = '.'
L = empty // branches
ends = []
last = (-1, -1)
for i in range(empty):
    if i % L == 0:
        # restart branch
        if i > 0:
            ends.append(last)
        starts = []
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '.':
                    score = random.random()
                    for j in range(4):
                        x2 = x + DX[j]
                        y2 = y + DY[j]
                        if x2 >= 0 and y2 >= 0 and x2 < n and y2 < m and grid[x2][y2] == '#':
                            score += 1.0
                    starts.append((score, (x, y)))
        starts.sort()
        last = starts[-1][1]
    blocked_neighbours = []
    other_neighbours = []

    neighbours = []

    for j in range(4):
        x = last[0] + DX[j]
        y = last[1] + DY[j]
        if x >= 1 and y >= 1 and x < n-1 and y < m-1:
            score = random.random()
            if grid[x][y] == '#':
                blocked_neighbours.append((x, y))
                score += 1
                for j2 in range(4):
                    x2 = x + DX[j2]
                    y2 = y + DY[j2]
                    if grid[x2][y2] == '#':
                        score += 1
            neighbours.append((score, (x, y)))
    neighbours.sort()
    (x, y) = neighbours[-1][1]
    last = (x, y)
    grid[x][y] = '.'
random.shuffle(ends)

for i in range(min(len(ends), k)):
    grid[ends[i][0]][ends[i][1]] = 'P'
    k -= 1
while k > 0:
    cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                cells.append((i, j))
    if len(cells) == 0:
        break
    cell = random.choice(cells)
    grid[cell[0]][cell[1]] = 'P'
    k -= 1

print(n,m)
for i in range(0, n):
    print("".join(grid[i]))
