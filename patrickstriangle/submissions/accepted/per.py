#!/usr/bin/env python3
import sys
input = sys.stdin.readline

MOD = 10**9 + 7
MAX = 10**6+1

fac = [1]*MAX
invfac = [1]*MAX
base = [1, 2, 1, 2, 1]
for i in range(1, MAX):
    fac[i] = (fac[i-1]*i) % MOD
    invfac[i] = pow(fac[i], MOD-2, MOD)
    assert fac[i] * invfac[i] % MOD == 1

def binom(n, k):
    if k < 0 or k > n: return 0
    return fac[n] * invfac[k] * invfac[n-k] % MOD
    
q = int(input())
for _ in range(q):
    (n, k, x) = map(int, input().split())
    val = sum(base[i]*binom(n-1, k+1-i) for i in range(5)) % MOD
    print(['Incorrect', 'Correct'][val == x])

