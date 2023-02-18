#!/bin/bash
USE_SCORING=0
. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution nils.cpp

compile gen_random.py
compile gen_cave.py
compile gen_zigzag.py
compile gen_diagonal.py

MAXN=100
MAXK=100

sample_manual 1
sample_manual 2
sample_manual 3

tc random-01 gen_random n=5 m=5 k=1 
tc random-02 gen_random n=5 m=30 k=4 walls=3
tc random-03 gen_random n=77 m=33 k=1 walls=0
tc random-04 gen_random n=100 m=100 k=100 walls=0
tc random-05 gen_random n=100 m=100 k=100 walls=100
tc random-06 gen_random n=100 m=100 k=100 walls=200
tc random-07 gen_random n=100 m=100 k=100 walls=300
tc random-08 gen_random n=100 m=100 k=100 walls=700
tc random-09 gen_random n=100 m=100 k=100 walls=4000
tc random-10 gen_random n=12 m=12 k=100

tc cave-11 gen_cave n=10 m=10 k=10 empty=10 branches=1
tc cave-12 gen_cave n=10 m=100 k=100 empty=100 branches=5
tc cave-13 gen_cave n=100 m=100 k=100 empty=100 branches=1
tc cave-14 gen_cave n=100 m=100 k=1 empty=3000 branches=1
tc cave-15 gen_cave n=100 m=100 k=100 empty=2000 branches=10
tc cave-16 gen_cave n=100 m=100 k=100 empty=2000 branches=40
tc cave-17 gen_cave n=100 m=100 k=100 empty=2000 branches=100
tc cave-18 gen_cave n=100 m=100 k=100 empty=8000 branches=30
tc cave-19 gen_cave n=100 m=100 k=100 empty=2000 branches=1
tc cave-20 gen_cave n=100 m=100 k=100 empty=6000 branches=1
tc cave-21 gen_cave n=100 m=100 k=100 empty=4000 branches=3

tc zigzag-22 gen_zigzag n=100 m=100 k=100
tc line-23 gen_random n=3 m=100 k=75
tc line-24 gen_random n=100 m=3 k=75
tc diagonal-25 gen_diagonal n=100 m=100 k=100
tc diagonal-26 gen_diagonal n=60 m=60 k=100