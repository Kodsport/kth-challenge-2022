#!/bin/bash
USE_SCORING=0
. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution nils.py

compile gen_random.py

MAXN=30000

sample_manual 1

tc random-01 gen_random n=1
tc random-02 gen_random n=100
tc random-03 gen_random n=$MAXN
