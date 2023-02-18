#!/usr/bin/env python3

n = int(input())
if n < 99: print(99)
else:
    lo = (n//100)*100-1
    hi = (n//100)*100+99
    if hi-n <= n-lo: print(hi)
    else: print(lo)
