#!/usr/bin/env python3

S1 = input()
S2 = input()
n1 = len(S1)
n2 = len(S2)

for i in range(1, n1+n2):
    if S1[:i] != S2[:i]:
        print(n1+n2-2*(i-1))
        break
else:
    print(0)    
