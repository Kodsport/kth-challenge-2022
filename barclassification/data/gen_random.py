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
vertical = int(cmdlinearg('vertical', -1))
flip = int(cmdlinearg('flip', 0))
mode = cmdlinearg('mode', 'random')

if vertical == -1:
    vertical = random.randint(0,1)

grid = [[0]*n for _ in range(n)]

if mode == "random":
    if vertical == 1:
        col = random.randrange(0, n)
        for i in range(n):
            grid[i][col] = 1
    else:
        row = random.randrange(0, n)
        for i in range(n):
            grid[row][i] = 1

    for _ in range(flip):
        i = random.randrange(0, n)
        j = random.randrange(0, n)
        grid[i][j] ^= 1
if mode == "plus":
    i = random.randrange(n)
    j = random.randrange(n)
    for x in range(n):
        for y in range(n):
            if x == i or y == j:
                grid[x][y] = 1
    if flip == 1:
        grid[i][j] = 0
if mode == "empty":
    flip = min(flip, 2)
    for _ in range(flip):
        i = random.randrange(n)
        j = random.randrange(n)
        grid[i][j] = 1

print(n)
for i in range(n):
    print("".join([str(c) for c in grid[i]]))

