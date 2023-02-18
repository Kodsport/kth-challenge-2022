#!/usr/bin/env python3
import random

n = int(input())
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz_"
seen = set()

while len(seen) < n:
    a = random.choice(consonants)
    b = random.choice(vowels)
    c = random.choice(consonants)
    d = random.choice(consonants)
    e = random.choice(vowels)
    s = a+b+c+d+e
    if s not in seen:
        print(s)
        seen.add(s)
    
