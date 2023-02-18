#!/usr/bin/env python3

import sys

N_BOUND = 2 * 10**5

assert_no_windows_newline = True
if assert_no_windows_newline:
    input = lambda: sys.stdin.buffer.readline().decode() # Will detect windows newline
else:
    input = lambda: sys.stdin.readline().replace('\r\n', '\n') # Will not detect windows newline

ln = input()
n = int(ln)

assert 1 <= n <= N_BOUND
assert str(n) + '\n' == ln

def read_pair():
    ln = input()
    A = [int(x) for x in ln.split()]
    
    assert ' '.join(map(str,A)) + '\n' == ln
    assert len(A) == 2
    assert all(1 <= a <= n for a in A)
    assert A[0] != A[1]

    return A


graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u,v = read_pair()
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

found = [0] * n
bfs = [0]
found[0] = 1
for node in bfs:
    for nei in graph[node]:
        if not found[nei]:
            found[nei] = 1
            bfs.append(nei)

assert all(found)

assert not sys.stdin.buffer.read().split()

exit(42)
