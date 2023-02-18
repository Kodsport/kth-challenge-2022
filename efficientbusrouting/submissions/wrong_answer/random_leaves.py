#!/usr/bin/env python3
import sys, random

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u,v = [int(x) - 1 for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

leaves = [i for i in range(n) if len(graph[i]) == 1]
random.seed(1337)
random.shuffle(leaves)

if len(leaves) & 1:
    leaves.append(leaves[0]);

print(len(leaves)//2)
for i in range(0, len(leaves), 2):
    u = leaves[i]
    v = leaves[i + 1]
    print(u + 1, v + 1)
