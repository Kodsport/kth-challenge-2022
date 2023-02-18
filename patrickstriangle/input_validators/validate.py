#!/usr/bin/env python3

import sys

Q_BOUND = 2*10**5
N_BOUND = 10**6

assert_no_windows_newline = False
if assert_no_windows_newline:
    inp = sys.stdin.buffer.read().decode()
else:
    inp = sys.stdin.read().replace('\r\n', '\n')

A = [int(x) for x in inp.split()]; ii = 0
correct_inp = []

q = A[ii]; ii += 1
assert 1 <= q <= Q_BOUND
correct_inp.append(str(q))

for _ in range(q):
    n,k,x = A[ii:ii+3]; ii += 3
    
    assert 1 <= k <= n <= N_BOUND
    assert 0 <= x < 10**9 + 7

    correct_inp.append("%d %d %d" % (n,k,x))


print(repr('\n'.join(correct_inp) + '\n'))
print(repr(inp)) # check formatting

assert '\n'.join(correct_inp) + '\n' == inp # check formatting

exit(42)
