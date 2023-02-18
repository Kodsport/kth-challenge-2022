#!/usr/bin/env python3

import sys
input = sys.stdin.readline
 
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u,v = [int(x) - 1 for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)


optimal_room = [0] * n

root = 0
for _ in range(3):
    dist = [-1] * n
    dist[root] = 0
    bfs = [root]
    for node in bfs:
        for nei in graph[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                bfs.append(nei)

    optimal_dist = max(dist)
    A = [i for i in range(n) if dist[i] == optimal_dist]
    for i in A:
        optimal_room[i] = 1
    root = i

A = [i for i in range(n) if optimal_room[i]]
print(*[a + 1 for a in A])
