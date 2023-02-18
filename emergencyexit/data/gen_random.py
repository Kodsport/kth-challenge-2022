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
walls = int(cmdlinearg('walls', 0))

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
random.shuffle(cells)
for i in range(0, len(cells)):
    x = cells[i][0]
    y = cells[i][1]
    if i < k:
        grid[x][y] = 'P'
    elif i >= k and i-k < walls:
        grid[x][y] = '#'
    else:
        grid[x][y] = '.'
grid[edge_cells[0][0]][edge_cells[0][1]] = '.'

print(n,m)
for i in range(0, n):
    print("".join(grid[i]))
