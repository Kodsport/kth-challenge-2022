#!/usr/bin/env python3

import sys

n = int(input())

edges = []
for _ in range(n - 1):
    u,v = [int(x) - 1 for x in input().split()]
    edges.append((u,v))

def calc_brute(bob, graph):
    dist = [-1] * n
    dist[bob] = 0
    bfs = [bob]

    for node in bfs:
        for nei in graph[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                bfs.append(nei)

    assert all(d >= 0 for d in dist)
    return sum(dist)

graph = [[] for _ in range(n)]
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

DP = [0] * n
for bob in range(n):
    DP[bob] = calc_brute(bob, graph)

opt = max(DP)
A = [i for i in range(n) if DP[i] == opt]

# Expected time for starting in room i is
# -0.5 + 1.5 * n - DP[i]/n
# where DP[i]/n is expected distance from room i and egg

print(len(A))
print(*[a + 1 for a in A])
