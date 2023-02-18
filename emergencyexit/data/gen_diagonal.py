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

grid[0][1] = '.'

for i in range(1, n-1):
    if k > 0:
        grid[n-1-i][i] = 'P'
        k -= 1

while k > 0:
    i = random.randint(1,n-1)
    j = random.randint(1,m-1)
    if grid[i][j] == '.' and i+j > n:
        grid[i][j] = 'P'
        k -= 1

print(n,m)
for i in range(0, n):
    print("".join(grid[i]))
