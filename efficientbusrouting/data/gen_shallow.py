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
random.seed((n,seed,1338))

edges = []
for v in range(1, n):
    u = random.randrange(v)
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
