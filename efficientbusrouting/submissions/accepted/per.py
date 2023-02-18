#!/usr/bin/env python3

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    (u, v) = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

    
def solve():
    if n == 1:
        print(0)
        return
    if n == 2:
        print(1)
        print('1 2')
        return
    root = next(x for x in range(n+1) if len(adj[x]) > 1)

    par = [0]*(n+1)
    Q = [root]
    L = [root]
    while Q:
        u = Q.pop()
        for v in adj[u]:
            if v != par[u]:
                par[v] = u
                Q.append(v)
                L.append(v)
                
    endpoints = [[] for _ in range(n+1)]
    routes = []
    while L:
        u = L.pop()
        if len(adj[u]) == 1:
            endpoints[u].append(u)
            continue

        Twos = [endpoints[v] for v in adj[u] if v != par[u] and len(endpoints[v]) == 2]
        Ones = [endpoints[v] for v in adj[u] if v != par[u] and len(endpoints[v]) == 1]
        while 2*len(Twos) + len(Ones) > 2:
            if Twos: X = Twos.pop()
            else:    X = Ones.pop()
            if Twos: Y = Twos.pop()
            else:    Y = Ones.pop()
            x = X.pop()
            y = Y.pop()
            routes.append((x, y))
            if X: Ones.append(X)
            if Y: Ones.append(Y)

        if Twos: endpoints[u] = Twos[0]
        else:
            for X in Ones: endpoints[u].append(X[0])

    if len(endpoints[root]) == 1: endpoints[root].append(root)
    routes.append((endpoints[root][0], endpoints[root][1]))

    print(len(routes))
    for (u, v) in routes: print(u, v)
    
solve()
