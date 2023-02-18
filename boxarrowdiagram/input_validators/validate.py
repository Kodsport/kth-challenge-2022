#!/usr/bin/env python3

import sys

Q_BOUND = 2*10**5
N_BOUND = 2*10**5
M_BOUND = 2*10**5

assert_no_windows_newline = False
if assert_no_windows_newline:
    inp = sys.stdin.buffer.read().decode()
else:
    inp = sys.stdin.read().replace('\r\n', '\n')

A = [int(x) for x in inp.split()]; ii = 0
correct_inp = []

n,m = A[ii:ii + 2]; ii += 2

assert 1 <= n <= N_BOUND
assert 1 <= m <= M_BOUND

correct_inp.append("%d %d" % (n,m))

for _ in range(m):
    u,v = A[ii: ii + 2]; ii += 2
    assert 1 <= u <= n
    assert 1 <= v <= m
    correct_inp.append("%d %d" % (u,v))

q = A[ii]; ii += 1
assert 1 <= q <= Q_BOUND
correct_inp.append(str(q))

deleted = [0] * m
for _ in range(q):
    x,y = A[ii: ii + 2]; ii += 2
    assert 1 <= x <= 2
    if x == 1:
        assert 1 <= y <= m
        assert not deleted[y - 1]
        deleted[y - 1] = 1
    else:
        assert 1 <= y <= n
    correct_inp.append("%d %d" % (x,y))

assert '\n'.join(correct_inp) + '\n' == inp # check formatting

exit(42)
