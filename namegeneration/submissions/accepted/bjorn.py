#!/usr/bin/env python3
import string

alpha = string.ascii_lowercase
vowel = 'aeiou'
consonant = ''.join(c for c in alpha if c not in vowel)

S = []

for c1 in consonant:
    for c2 in vowel:
        for c3 in consonant:
            for c4 in consonant:
                S.append(c1 + c2 + c3 + c4)

print(*S[:int(input())], sep='\n')
