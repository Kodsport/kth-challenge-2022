#!/usr/bin/env python3

import sys
input = sys.stdin.readline
 
def exclusive(A, base, f, node):
    n = len(A)
 
    B = [base] * n
    for bit in reversed(range(n.bit_length())):
        for i in reversed(range(n)):
            B[i] = B[i // 2]
        for i in range(n & ~(bit == 0)):
            ind = (i >> bit) ^ 1
            B[ind] = f(B[ind], A[i], node, i)
    return B
 
def rerooter(graph, base, f , g = lambda x,node,eind: x):
    n = len(graph)
    rootDP = list(base)
    forward_edge_DP = [None] * n
    backward_edge_DP = [None] * n

    if n == 1:
        return [g(base[0], 0, -1)], [[]], [[]]

    P = [-1] * n
    P[0] = 0
    bfs = [0]
    for node in bfs:
        for nei in graph[node]:
            if P[nei] == -1:
                P[nei] = node
                bfs.append(nei)
 
    DP = [g(base[bfs[-1]], bfs[-1], -1)] * n
    for node in reversed(bfs):
        accumDP = base[node]
        for eind, nei in enumerate(graph[node]):
            if P[node] != nei:
                accumDP = f(accumDP, DP[nei], node, eind)
        DP[node] = g(accumDP, node, graph[node].index(P[node]) if node else -1)
    
    for node in bfs:
        DP[P[node]] = DP[node]
        forward_edge_DP[node] = [DP[nei] for nei in graph[node]]
 
        accumDP = exclusive(forward_edge_DP[node], base[node], f, node)
        rootDP[node] = g(f(accumDP[0], forward_edge_DP[node][0], node, 0), node, -1)
        backward_edge_DP[node] = [g(dp, node, eind) for eind, dp in enumerate(accumDP)]
        for nei, dp in zip(graph[node], backward_edge_DP[node]):
            DP[nei] = dp
    return rootDP, forward_edge_DP, backward_edge_DP
 
 
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u,v = [int(x) - 1 for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

# DP state contains 2 integers
# subtree size - 1
# sum of subtree size - 1 over subtree

def f(nodeDP, neiDP, node, eind):
  return nodeDP[0] + neiDP[0] + 1, nodeDP[1] + neiDP[1]
 
def g(nodeDP, node, eind):
  return nodeDP[0], nodeDP[1] + nodeDP[0]

rootDP, _, _ = rerooter(graph, [(0,0)] * n, f, g)
DP = [dp[1] for dp in rootDP]

# Expected time for starting in room i is
# -0.5 + 1.5 * n - DP[i]/n
# where DP[i]/n is expected distance from room i and egg

opt = max(DP)
A = [i for i in range(n) if DP[i] == opt]
print(len(A))
print(*[a + 1 for a in A])
