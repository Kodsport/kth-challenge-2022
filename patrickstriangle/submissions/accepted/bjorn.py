#!/usr/bin/env python3

MOD = 10 ** 9 + 7 # needs to be prime!
maxN = 10 ** 6 + 10    # needs to be <= MOD

def modmul(a, b, c=0):
    return (a * b + c) % MOD


""" Precalculate factorial, inverse factorial and modular inverse """
def mod_precalc(n):
    """ Calculates fac, inv_fac and (modular) inv for i < n in O(n) time """
    assert n <= MOD
    
    fac = [1] * n
    for i in range(2, n):
        fac[i] = modmul(fac[i - 1], i)

    inv_fac = [pow(fac[-1], MOD - 2, MOD)] * n
    for i in reversed(range(1, n)):
        inv_fac[i - 1] = modmul(inv_fac[i], i)

    inv = [modmul(inv_fac[i], fac[i - 1]) for i in range(n)]

    return fac, inv_fac, inv
fac, inv_fac, inv = mod_precalc(maxN)


def choose(n, k):
    """ Calculate n choose k in O(1) time """
    if k < 0 or k > n:
        return 0
    return modmul(modmul(fac[n], inv_fac[k]), inv_fac[n - k])

def patrick(n,k):
    if k < 0 or k > n:
        return 0
    y = (+ choose(n+1,k+2)
         + choose(n+1,k+1)
         - choose(n, k)
         + choose(n+1,k)
         + choose(n+1,k-1)
        ) % MOD
    return y

### SOLUTION
import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n,k,x = [int(x) for x in input().split()]

    n -= 1
    k -= 1

    y = patrick(n, k)
    if x == y:
        print('Correct')
    else:
        print('Incorrect')
