#!/usr/bin/env python3

(n, m) = map(int, input().split())

edges = [None]
removed = [0]*(m+1)
adj = [[] for _ in range(n+1)]

for i in range(m):
    (u, v) = map(int, input().split())
    edges.append((u, v))

q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]
for (op, y) in queries:
    if op == 1: removed[y] = True

alive = [0]*(n+1)
refcount = [0]*(n+1)
alive[1] = True

def add(u, v):
    adj[u].append(v)
    if alive[u]:
        refcount[v] += 1
    if alive[u] and not alive[v]:
        alive[v] = True
        Q = [v]
        while Q:
            v = Q.pop()
            for w in adj[v]:
                refcount[w] += 1
                if not alive[w]:
                    alive[w] = True
                    Q.append(w)

for i in range(1, m+1):
    if not removed[i]:
        add(edges[i][0], edges[i][1])
        
answers = []
for (op, y) in reversed(queries):
    if op == 1:
        add(edges[y][0], edges[y][1])
    else:
        answers.append(refcount[y])

for x in reversed(answers):
    print(x)
