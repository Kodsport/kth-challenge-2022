#!/usr/bin/env python3
import os

S1 = input()
S2 = input()

Spre = os.path.commonprefix([S1, S2])

print(len(S1) + len(S2) - 2 * len(Spre))
