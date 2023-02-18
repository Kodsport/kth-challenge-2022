#!/usr/bin/env python3


"""
This solution does not keep track of how many references each node has,
instead it calculates it whenever needed.

Should run q*m for well designed input.

"""


import sys
input = sys.stdin.readline

n,m = [int(x) for x in input().split()]

edges = []
for _ in range(m):
    u,v = [int(x) - 1 for x in input().split()]
    edges.append((u,v))

q = int(input())

queries = []
to_be_removed = [0] * m # Which edges are queried to be removed
for _ in range(q):
    x,y = [int(x) for x in input().split()]
    y -= 1
    queries.append((x, y))
    if x == 1:
        to_be_removed[y] = 1

# Add the rest to be removed at the end
for y in range(m):
    if not to_be_removed[y]:
        queries.append((1, y))


out = []
reachable = [0] * n
reachable[0] = 1

graph = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]

for x,y in reversed(queries):
    if x == 1:
        u,v = edges[y]
        graph[u].append(v)
        graph2[v].append(u)
        if reachable[u]:
            bfs = [u]
            for node in bfs:
                for nei in graph[node]:
                    if not reachable[nei]:
                        reachable[nei] = 1
                        bfs.append(nei)
                del graph[node][:]
    else:
        out.append(sum(reachable[node] for node in graph2[y]))


out.reverse()
print('\n'.join(str(x) for x in out))
