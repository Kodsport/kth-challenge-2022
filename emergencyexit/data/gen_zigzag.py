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

grid = []
for i in range(n):
    row = []
    for j in range(m):
        if i == 0 or j == 0 or i == n-1 or j == m-1:
            row.append('#')
        else:
            row.append('.')
    grid.append(row)

grid[0][2] = '.'
diag = 4
diags = 0
while diag <= n+m:
    cells = []
    cell = (diag, 0)
    for _ in range(n+m):
        if 1 <= cell[0] <= n-2 and 1 <= cell[1] <= m-2:
            cells.append(cell)
            grid[cell[0]][cell[1]] = '#'
        cell = (cell[0]-1, cell[1]+1)
    if len(cells) == 0:
        break
    if diags%2 == 0:
        grid[cells[0][0]][cells[0][1]] = '.'
    else:
        grid[cells[-1][0]][cells[-1][1]] = '.'
    diags += 1
    diag += 3

empty = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            empty.append((i+j, (i, j)))
empty.sort(reverse=True)

for i in range(k):
    (x, y) = empty[i][1]
    grid[x][y] = 'P'

print(n,m)
for i in range(0, n):
    print("".join(grid[i]))
