#!/usr/bin/env python3
n = int(input())
if n < 100 or n%100 >= 49:
    print(n-n%100+99)
else:
    print(n-n%100-1)
    