#!/usr/bin/env python3

import sys
import string

N_MIN_BOUND = 1
N_MAX_BOUND = 100
ALPHA = string.ascii_lowercase

inp = sys.stdin.read()
S1, S2 = inp.split()

assert N_MIN_BOUND <= len(S1) <= N_MAX_BOUND
assert N_MIN_BOUND <= len(S2) <= N_MAX_BOUND

assert all(c in ALPHA for c in S1)
assert all(c in ALPHA for c in S2)

assert '\n'.join((S1, S2)) + '\n' == inp # check formatting

exit(42)
