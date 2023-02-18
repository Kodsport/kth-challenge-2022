#!/usr/bin/env python3

def cmdlinearg(name, default=None):
    import sys
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

n = int(cmdlinearg('n'))
seed = int(cmdlinearg('seed'))
exact = int(cmdlinearg('exact'))

import random
random.seed((seed, n, exact))

if not exact:
    m = random.randint(1, n)
    n = random.randint(1, n)
else:
    m = n

common_prefix_len = random.randrange(min(n,m) + 1)

def random_string(n):
    import string
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

Spre = random_string(common_prefix_len)
S1 = Spre + random_string(n - common_prefix_len)
S2 = Spre + random_string(m - common_prefix_len)

print(S1)
print(S2)
