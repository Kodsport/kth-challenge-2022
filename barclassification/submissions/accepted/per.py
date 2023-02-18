#!/usr/bin/env python3

n = int(input())
grid = [list(map(int, input().strip())) for _ in range(n)]

row_ones = [0]*n
col_ones = [0]*n
ones = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            row_ones[i] += 1
            col_ones[j] += 1
            ones += 1

horz = vert = False
for i in range(n):
    if ones-row_ones[i] + (n-row_ones[i]) <= n: horz = True
for j in range(n):
    if ones-col_ones[j] + (n-col_ones[j]) <= n: vert = True

if horz and vert:
    print('+')
elif horz:
    print('-')
elif vert:
    print('|')
else:
    assert False
