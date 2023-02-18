#!/bin/bash
USE_SCORING=0
. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution nils.py

compile gen_random.py

MAXN=10000

sample_manual 1
sample_manual 2
sample_manual 3

tc case-01 gen_random n=1
tc case-02 gen_random n=2
tc case-03 gen_random n=48
tc case-04 gen_random n=100
tc case-05 gen_random n=148
tc case-06 gen_random n=149
tc case-07 gen_random n=150
tc case-08 gen_random n=198
tc case-09 gen_random n=411
tc case-10 gen_random n=1049
tc case-11 gen_random n=2375
tc case-12 gen_random n=$(($MAXN - 100))
tc case-13 gen_random n=$(($MAXN - 52))
tc case-14 gen_random n=$(($MAXN - 51))
tc case-15 gen_random n=$(($MAXN - 50))
tc case-16 gen_random n=$(($MAXN - 13))
