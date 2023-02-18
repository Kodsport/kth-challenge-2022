#!/usr/bin/env python3
import sys

(n, m) = map(int, input().split())

grid = [input() for _ in range(n)]

sr = sc = 0
for i in range(n):
    if grid[i][0] != '#':
        sr = i
        out = 'L'
    elif grid[i][-1] != '#':
        (sr, sc) = (i, m-1)
        out = 'R'
for i in range(m):
    if grid[0][i] != '#':
        sc = i
        out = 'U'
    elif grid[-1][i] != '#':
        (sr, sc) = (n-1, i)
        out = 'D'

Q = [(sr, sc)]
dist = [[1<<30]*m for _ in range(n)]
dist[sr][sc] = 0
qh = 0
while qh < len(Q):
    (r, c) = Q[qh]
    qh += 1
    for (nr, nc) in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#' and dist[nr][nc] == 1<<30:
            dist[nr][nc] = dist[r][c] + 1
            Q.append((nr, nc))

pos = []
bad = False
for r in range(n):
    for c in range(m):
        if grid[r][c] == 'P':
            pos.append((r, c))
            bad |= dist[r][c] == 1<<30

if bad:
    print('-1')
    sys.exit(0)
    
P = len(pos)
rem = P
instrs = [[] for _ in range(P)]

while rem > 0:
    newpos = set()
    for i in sorted(range(P), key = lambda i: dist[pos[i][0]][pos[i][1]] if pos[i] else -1):
        if not pos[i]:
            instrs[i].append('.')
            continue
        (r, c) = pos[i]
        if (r, c) == (sr, sc):
            instrs[i].append(out)
            pos[i] = None
            rem -= 1
        else:
            for (nr, nc, d) in [(r+1, c, 'D'), (r-1, c, 'U'), (r, c-1, 'L'), (r, c+1, 'R')]:
                if dist[nr][nc] < dist[r][c] and (nr, nc) not in newpos:
                    instrs[i].append(d)
                    newpos.add((nr, nc))
                    pos[i] = (nr, nc)
                    break
            else:
                newpos.add((r, c))
                instrs[i].append('.')

print(len(instrs[0]))
for I in instrs:
    print(''.join(I))

        
