#!/usr/bin/env python3

import sys

n,m = [int(x) for x in input().split()]

mat = [input() for _ in range(n)]
mat2 = [row.replace('P', '.') for row in mat]

for i in range(n):
    for j in range(m):
        if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and mat2[i][j] == '.':
            break
    else:
        continue
    break

bfs = [(i,j)]
dist = [[-1] * m for _ in range(n)]
dist[i][j] = 1

for i,j in bfs:
    for di,dj in (i+1,j), (i-1,j), (i,j+1), (i,j-1):
        if 0 <= di < n and 0 <= dj < m and dist[di][dj] == -1 and mat2[di][dj] == '.':
            dist[di][dj] = dist[i][j] + 1
            bfs.append((di, dj))


people = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'P':
            people.append((i,j))


if any(dist[i][j] == -1 for i,j in people):
    print(-1)
    sys.exit()

def dist_calc(ind):
    i,j = people[ind]
    return dist[i][j]

k = len(people)
order = sorted(range(k), key = dist_calc)


prev = -1
timer = [-1] * k
for p_ind in order:
    i,j = people[p_ind]
    d = dist[i][j]
    prev = max(d, prev + 1)
    timer[p_ind]= prev

max_t = max(timer)
print(max_t)
for p_ind in range(k):
    i,j = people[p_ind]
    walk = ['.' * (timer[p_ind] - dist[i][j])]
    
    while 0 <= i < n and 0 <= j < m:
        di,dj = i+1,j
        if not (0 <= di < n and 0 <= dj < m) or dist[di][dj] == dist[i][j] - 1:
            walk.append('D')
            i,j = di,dj
            continue
        
        di,dj = i-1,j
        if not (0 <= di < n and 0 <= dj < m) or dist[di][dj] == dist[i][j] - 1:
            walk.append('U')
            i,j = di,dj
            continue
        
        di,dj = i,j+1
        if not (0 <= di < n and 0 <= dj < m) or dist[di][dj] == dist[i][j] - 1:
            walk.append('R')
            i,j = di,dj
            continue

        di,dj = i,j-1
        if not (0 <= di < n and 0 <= dj < m) or dist[di][dj] == dist[i][j] - 1:
            walk.append('L')
            i,j = di,dj
            continue

    walk.append('.' * (max_t - timer[p_ind]))
    
    print(''.join(walk))
