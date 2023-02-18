#!/usr/bin/env python3

import sys
import random

def cmdlinearg(name, default=None):
    import sys
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

n = int(cmdlinearg('n'))
seed = int(cmdlinearg('seed'))
random.seed((n,seed,1341))


nodes = list(range(n))

mid = nodes[:len(nodes)//2]
del nodes[:len(nodes)//2]


binary1 = [mid[0]] + nodes[:len(nodes)//2]
del nodes[:len(nodes)//2]

binary2 = [mid[-1]] + nodes

edges = []
for i in range(len(mid) - 1):
    edges.append((mid[i], mid[i + 1]))

for binary in binary1, binary2:
    for i in range(1, len(binary)):
        u = binary[i // 2]
        v = binary[i]
        edges.append((u,v))

def shuffler(A):
    A = list(A)
    random.shuffle(A)
    return A

def shuffle_edges(edges):
    permutation = shuffler(range(n))
    edges = [[permutation[x] for x in e] for e in edges]
    edges = [shuffler(e) for e in edges]
    edges = shuffler(edges)
    return edges

edges = shuffle_edges(edges)
print(n)
for u,v in edges:
    print(u + 1, v + 1)
