#!/bin/bash
USE_SCORING=0
. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution nils.cpp

compile gen_random.py

MAXN=1000

sample_manual 1
sample_manual 2
sample_manual 3

tc random-01 gen_random n=2
tc random-02 gen_random n=2 flip=1
tc random-03 gen_random n=100 vertical=1
tc random-04 gen_random n=100 vertical=0
tc random-05 gen_random n=100 vertical=1 flip=100
tc random-06 gen_random n=100 vertical=0 flip=100
tc random-07 gen_random n=1000 vertical=1
tc random-08 gen_random n=1000 vertical=0
tc random-09 gen_random n=1000 vertical=1 flip=1000
tc random-10 gen_random n=1000 vertical=0 flip=1000
tc random-11 gen_random n=1000 mode=plus
tc random-12 gen_random n=1000 mode=empty
tc random-13 gen_random n=1000 mode=empty flip=2
tc random-14 gen_random n=100 mode=plus flip=1
tc_manual ../manual_tests/diag1.in
tc_manual ../manual_tests/diag2.in
tc_manual ../manual_tests/diag3.in
tc_manual ../manual_tests/cross1.in
tc_manual ../manual_tests/cross2.in
