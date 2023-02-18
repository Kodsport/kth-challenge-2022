#!/usr/bin/env python3

def cmdlinearg(name, default=None):
    import sys
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

n = int(cmdlinearg('n'))
m = int(cmdlinearg('m'))
q = int(cmdlinearg('q'))
seed = int(cmdlinearg('seed'))

import random
random.seed((seed, 1337))

node_perm = list(range(1,n))
random.shuffle(node_perm)
node_perm = [0] + node_perm

edge_perm = list(range(m))
random.shuffle(edge_perm)
inv_edge_perm = [-1] * m
for i in range(m):
    inv_edge_perm[edge_perm[i]] = i

def transform_edges(edges):
    edges = [edges[i] for i in edge_perm]
    edges = [[node_perm[j] for j in e] for e in edges]
    return edges

print(n,m)

edges = []
for _ in range(m - n):
    u = random.randrange(n)
    edges.append((0, u))

edges.append((0,1))

edges2 = []
for i in range(1, n - 1):
    edges2.append((i, i + 1))
edges2.append((n - 1, 1))
random.shuffle(edges2)
edges += edges2

edges = transform_edges(edges)
for u,v in edges:
    print(u + 1, v + 1)

print(q)
queries = []
e = 0 
for _ in range(q):
    if _&1 and e < m:
        print(1, inv_edge_perm[e] + 1)
        e += 1
    else:
        u = random.randrange(n)
        print(2, node_perm[u] + 1)
