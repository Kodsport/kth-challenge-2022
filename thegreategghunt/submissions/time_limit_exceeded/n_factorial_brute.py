#!/usr/bin/env python3

import sys
import itertools

n = int(input())

edges = []
for _ in range(n - 1):
    u,v = [int(x) - 1 for x in input().split()]
    edges.append((u,v))


def calc_brute(bob, egg, graph):
    count = 0
    final_count = -10**9

    explored = [0] * n
    def dfs(node):
        nonlocal count
        nonlocal final_count

        count += 1
        explored[node] = 1
        
        if node == egg:
            final_count = count

        for nei in graph[node]:
            if explored[nei]:
                continue
            count += 1
            dfs(nei)
            count += 1
    
    dfs(bob)
    return final_count

DP = [0] * n
for edge_perm in itertools.permutations(edges):
    graph = [[] for _ in range(n)]
    for u,v in edge_perm:
        graph[u].append(v)
        graph[v].append(u)

    for bob in range(n):
        for egg in range(n):
            DP[bob] += calc_brute(bob, egg, graph)

# Expected time for starting in room i is
# -0.5 + 1.5 * n - DP[i]/n!
# where DP[i]/n! is expected distance from room i and egg

opt = min(DP)
A = [i for i in range(n) if DP[i] == opt]


print(len(A))
print(*[a + 1 for a in A])
