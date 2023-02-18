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
random.seed((n,seed,1337))

assert n >= 7

edges = []
edges.append((0,2))
edges.append((1,2))
edges.append((5,2))
edges.append((3,4))
edges.append((4,5))
for i in range(6, n):
    edges.append((i - 1, i))

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
