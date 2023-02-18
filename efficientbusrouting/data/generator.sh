#!/bin/bash
USE_SCORING=0
. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution bjorn.py

compile gen_random.py
compile gen_wide.py
compile gen_shallow.py
compile gen_star.py
compile gen_multi_star.py
compile gen_binary.py
compile gen_two_binary.py
compile gen_fork.py

sample_manual 1
sample_manual 2

tc_manual ../manual_tests/tricky.in

tc small-002 gen_shallow seed=3 n=3
tc small-003 gen_shallow seed=2 n=3
tc small-004 gen_shallow seed=1 n=3

tc small-005 gen_random seed=1 n=10
tc small-006 gen_random seed=2 n=10
tc small-007 gen_random seed=8 n=10
tc small-008 gen_random seed=4 n=10
tc small-009 gen_random seed=9 n=10
tc small-010 gen_random seed=11 n=10
tc small-011 gen_random seed=7 n=10

tc random-012 gen_random seed=1 n=200000
tc random-013 gen_random seed=2 n=200000
tc random-014 gen_random seed=3 n=200000
tc random-015 gen_random seed=4 n=200000
tc random-016 gen_random seed=5 n=200000

tc wide-017 gen_wide seed=1 n=20 
tc wide-018 gen_wide seed=2 n=131071
tc wide-019 gen_wide seed=3 n=131072
tc wide-020 gen_wide seed=4 n=131073
tc wide-021 gen_wide seed=5 n=151072
tc wide-022 gen_wide seed=6 n=200000

tc shallow-023 gen_shallow seed=1 n=20 
tc shallow-024 gen_shallow seed=2 n=131071
tc shallow-025 gen_shallow seed=3 n=131072
tc shallow-026 gen_shallow seed=4 n=131073
tc shallow-027 gen_shallow seed=5 n=151072
tc shallow-028 gen_shallow seed=6 n=200000

tc star-029 gen_star seed=1 n=20 
tc star-030 gen_star seed=2 n=131071
tc star-031 gen_star seed=3 n=131072
tc star-032 gen_star seed=4 n=131073
tc star-033 gen_star seed=5 n=151072
tc star-034 gen_star seed=6 n=200000

tc multi_star-035 gen_multi_star seed=1 n=20     stars=5
tc multi_star-036 gen_multi_star seed=2 n=131071 stars=5
tc multi_star-037 gen_multi_star seed=3 n=131072 stars=5
tc multi_star-038 gen_multi_star seed=4 n=131073 stars=5
tc multi_star-039 gen_multi_star seed=5 n=151072 stars=5
tc multi_star-040 gen_multi_star seed=6 n=200000 stars=5

tc binary-041 gen_binary seed=1 n=20 
tc binary-042 gen_binary seed=2 n=131071
tc binary-043 gen_binary seed=3 n=131072
tc binary-044 gen_binary seed=4 n=131073
tc binary-045 gen_binary seed=5 n=151072
tc binary-046 gen_binary seed=6 n=200000

tc two-binary-047 gen_two_binary seed=1 n=20 
tc two-binary-048 gen_two_binary seed=2 n=131071
tc two-binary-049 gen_two_binary seed=3 n=131072
tc two-binary-050 gen_two_binary seed=4 n=131073
tc two-binary-051 gen_two_binary seed=5 n=151072
tc two-binary-052 gen_two_binary seed=6 n=200000

tc fork-053 gen_fork seed=1 n=200000
tc fork-054 gen_fork seed=2 n=200000
tc fork-055 gen_fork seed=3 n=200000
tc fork-056 gen_fork seed=4 n=200000
tc fork-057 gen_fork seed=5 n=200000
tc fork-058 gen_fork seed=6 n=200000
tc fork-059 gen_fork seed=7 n=200000
tc fork-060 gen_fork seed=8 n=200000

tc fork-061 gen_fork seed=1 n=7
tc fork-062 gen_fork seed=2 n=7
tc fork-063 gen_fork seed=3 n=7
tc fork-064 gen_fork seed=4 n=7
tc fork-065 gen_fork seed=5 n=7
tc fork-066 gen_fork seed=6 n=7
tc fork-067 gen_fork seed=7 n=7
tc fork-068 gen_fork seed=8 n=7
tc fork-069 gen_fork seed=9 n=7
tc fork-070 gen_fork seed=10 n=7
tc fork-071 gen_fork seed=11 n=7
tc fork-072 gen_fork seed=12 n=7
tc fork-073 gen_fork seed=13 n=7
tc fork-074 gen_fork seed=14 n=7
tc fork-075 gen_fork seed=15 n=7
tc fork-076 gen_fork seed=16 n=7
tc fork-077 gen_fork seed=17 n=7
tc fork-078 gen_fork seed=18 n=7
tc fork-079 gen_fork seed=19 n=7
tc fork-080 gen_fork seed=20 n=7
tc fork-081 gen_fork seed=21 n=7
tc fork-082 gen_fork seed=22 n=7
tc fork-083 gen_fork seed=23 n=7
tc fork-084 gen_fork seed=24 n=7
tc fork-085 gen_fork seed=25 n=7
tc fork-086 gen_fork seed=26 n=7
tc fork-087 gen_fork seed=27 n=7
tc fork-088 gen_fork seed=28 n=7
tc fork-089 gen_fork seed=29 n=7
tc fork-090 gen_fork seed=30 n=7
