#!/bin/bash
USE_SCORING=0
. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution bjorn.py

compile gen_random.py
compile gen_random_sparse.py
compile gen_row.py

sample_manual 1

tc random-01 gen_random n=5       q=10000 
tc random-02 gen_random n=100     q=10000 
tc random-03 gen_random n=1000000 q=10000 
tc random-04 gen_random n=5       q=200000 
tc random-05 gen_random n=100     q=200000 
tc random-06 gen_random n=1000000 q=200000 

tc random-sparse-07  gen_random_sparse n=5       q=10000 
tc random-sparse-08  gen_random_sparse n=100     q=10000 
tc random-sparse-09  gen_random_sparse n=1000000 q=10000 
tc random-sparse-010 gen_random_sparse n=5       q=200000 
tc random-sparse-011 gen_random_sparse n=100     q=200000 
tc random-sparse-012 gen_random_sparse n=1000000 q=200000 

tc row-013 gen_row n=999998    q=200000
tc row-014 gen_row n=999999    q=200000
tc row-015 gen_row n=1000000   q=200000
