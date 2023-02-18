#!/bin/bash
USE_SCORING=0
. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution bjorn.py

compile gen_random.py

sample_manual 1
sample_manual 2
sample_manual 3

tc random-001 gen_random seed=1  n=100 exact=0 
tc random-002 gen_random seed=2  n=100 exact=0 
tc random-003 gen_random seed=3  n=100 exact=0 
tc random-004 gen_random seed=4  n=100 exact=0 
tc random-005 gen_random seed=5  n=100 exact=0 
tc random-006 gen_random seed=6  n=100 exact=0 
tc random-007 gen_random seed=7  n=100 exact=0 
tc random-008 gen_random seed=8  n=100 exact=0 
tc random-009 gen_random seed=9  n=100 exact=0 
tc random-010 gen_random seed=10 n=100 exact=0 
tc random-011 gen_random seed=11 n=100 exact=0 
tc random-012 gen_random seed=12 n=100 exact=0 
tc random-013 gen_random seed=13 n=100 exact=0 
tc random-014 gen_random seed=14 n=100 exact=0 
tc random-015 gen_random seed=15 n=100 exact=0 
tc random-016 gen_random seed=16 n=100 exact=0 
tc random-017 gen_random seed=17 n=100 exact=0 
tc random-018 gen_random seed=18 n=100 exact=0 
tc random-019 gen_random seed=19 n=100 exact=0 
tc random-020 gen_random seed=20 n=100 exact=0 

tc random-021 gen_random seed=21 n=5 exact=0    
tc random-022 gen_random seed=22 n=5 exact=0 
tc random-023 gen_random seed=23 n=5 exact=0 
tc random-024 gen_random seed=24 n=5 exact=0 
tc random-025 gen_random seed=25 n=5 exact=0 
tc random-026 gen_random seed=26 n=5 exact=0 
tc random-027 gen_random seed=27 n=5 exact=0 
tc random-028 gen_random seed=28 n=5 exact=0 
tc random-029 gen_random seed=29 n=5 exact=0 
tc random-030 gen_random seed=30 n=5 exact=0 
tc random-031 gen_random seed=31 n=5 exact=0 
tc random-032 gen_random seed=32 n=5 exact=0 
tc random-033 gen_random seed=33 n=5 exact=0 
tc random-034 gen_random seed=34 n=5 exact=0 
tc random-035 gen_random seed=35 n=5 exact=0 
tc random-036 gen_random seed=36 n=5 exact=0 
tc random-037 gen_random seed=37 n=5 exact=0 
tc random-038 gen_random seed=38 n=5 exact=0 
tc random-039 gen_random seed=39 n=5 exact=0 
tc random-040 gen_random seed=40 n=5 exact=0 
tc random-041 gen_random seed=41 n=5 exact=0

tc random-042 gen_random seed=1  n=100 exact=1 
tc random-043 gen_random seed=2  n=100 exact=1
tc random-044 gen_random seed=3  n=100 exact=1
tc random-045 gen_random seed=4  n=100 exact=1
tc random-046 gen_random seed=5  n=100 exact=1
tc random-047 gen_random seed=6  n=100 exact=1
tc random-048 gen_random seed=7  n=100 exact=1
tc random-049 gen_random seed=8  n=100 exact=1
tc random-050 gen_random seed=9  n=100 exact=1
tc random-051 gen_random seed=10 n=100 exact=1
tc random-052 gen_random seed=11 n=100 exact=1
tc random-053 gen_random seed=12 n=100 exact=1
tc random-054 gen_random seed=13 n=100 exact=1
tc random-055 gen_random seed=14 n=100 exact=1
tc random-056 gen_random seed=15 n=100 exact=1
tc random-057 gen_random seed=16 n=100 exact=1
tc random-058 gen_random seed=17 n=100 exact=1
tc random-059 gen_random seed=18 n=100 exact=1
tc random-060 gen_random seed=19 n=100 exact=1
tc random-061 gen_random seed=20 n=100 exact=1

tc random-062 gen_random seed=21 n=5 exact=1
tc random-063 gen_random seed=22 n=5 exact=1
tc random-064 gen_random seed=23 n=5 exact=1
tc random-065 gen_random seed=24 n=5 exact=1
tc random-066 gen_random seed=25 n=5 exact=1
tc random-067 gen_random seed=26 n=5 exact=1
tc random-068 gen_random seed=27 n=5 exact=1
tc random-069 gen_random seed=28 n=5 exact=1
tc random-070 gen_random seed=29 n=5 exact=1
tc random-071 gen_random seed=30 n=5 exact=1
tc random-072 gen_random seed=31 n=5 exact=1
tc random-073 gen_random seed=32 n=5 exact=1
tc random-074 gen_random seed=33 n=5 exact=1
tc random-075 gen_random seed=34 n=5 exact=1
tc random-076 gen_random seed=35 n=5 exact=1
tc random-077 gen_random seed=36 n=5 exact=1
tc random-078 gen_random seed=37 n=5 exact=1
tc random-079 gen_random seed=38 n=5 exact=1
tc random-080 gen_random seed=39 n=5 exact=1
tc random-081 gen_random seed=40 n=5 exact=1
tc random-082 gen_random seed=41 n=5 exact=1

