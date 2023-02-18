#!/usr/bin/env python3
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u,v = [int(x) - 1 for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

num_leaves = sum(len(graph[i]) == 1 for i in range(n))

root = 0
while len(graph[root]) == 1: root += 1

bfs = [root]
for node in bfs:
    for nei in graph[node]:
        graph[nei].remove(node)
    bfs += graph[node]

paths = [[] for i in range(n)]

bus_lines = []
for node in reversed(bfs):
    if not graph[node]:
        paths[node].append(node)
        continue
    
    cur = []
    for nei in graph[node]:
        for leaf in paths[nei]:
            if len(cur) == 2:
                bus_lines.append((cur.pop(0), leaf))
            else:
                cur.append(leaf)
    paths[node] = cur

cur = paths[root]
if len(cur) == 2:
    bus_lines.append((cur.pop(), cur.pop()))
elif cur:
    bus_lines.append((root, cur.pop()))


print(len(bus_lines))
for u,v in bus_lines[:-1]:
    print(u + 1, v + 1)
