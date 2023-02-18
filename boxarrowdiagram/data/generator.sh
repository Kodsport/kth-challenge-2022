#!/bin/bash
USE_SCORING=0
. ../../testdata_tools/gen.sh

# For unlimited stack:
# ulimit -s unlimited

use_solution bjorn.py

compile gen_full.py
compile gen_star.py
compile gen_deep.py
compile gen_cycle.py
compile gen_all_queries.py

sample_manual 1

tc full-001 gen_full seed=1 n=100 m=200000 q=200000 
tc full-002 gen_full seed=2 n=100 m=200000 q=200000
tc full-003 gen_full seed=3 n=100 m=200000 q=200000
tc full-004 gen_full seed=4 n=100 m=200000 q=200000
tc full-005 gen_full seed=5 n=100 m=200000 q=200000
tc full-006 gen_full seed=6 n=100 m=200000 q=200000

tc star-007 gen_star seed=1 n=100000 m=200000 q=200000
tc star-008 gen_star seed=2 n=100000 m=200000 q=200000
tc star-009 gen_star seed=3 n=100000 m=200000 q=200000
tc star-010 gen_star seed=4 n=100000 m=200000 q=200000
tc star-011 gen_star seed=5 n=100000 m=200000 q=200000
tc star-012 gen_star seed=6 n=100000 m=200000 q=200000

tc deep-013 gen_deep seed=1 n=200000 m=200000 q=200000
tc deep-014 gen_deep seed=2 n=200000 m=200000 q=200000
tc deep-015 gen_deep seed=3 n=200000 m=200000 q=200000
tc deep-016 gen_deep seed=4 n=200000 m=200000 q=200000
tc deep-017 gen_deep seed=5 n=200000 m=200000 q=200000
tc deep-018 gen_deep seed=6 n=200000 m=200000 q=200000

tc cycle-019 gen_cycle seed=1 n=100000 m=200000 q=200000
tc cycle-020 gen_cycle seed=2 n=100000 m=200000 q=200000
tc cycle-021 gen_cycle seed=3 n=100000 m=200000 q=200000
tc cycle-022 gen_cycle seed=4 n=100000 m=200000 q=200000
tc cycle-023 gen_cycle seed=5 n=100000 m=200000 q=200000

tc cycle-024 gen_cycle seed=1 n=10 m=200000 q=200000
tc cycle-025 gen_cycle seed=2 n=10 m=200000 q=200000
tc cycle-026 gen_cycle seed=3 n=10 m=200000 q=200000
tc cycle-027 gen_cycle seed=4 n=10 m=200000 q=200000
tc cycle-028 gen_cycle seed=5 n=10 m=200000 q=200000

tc all_queries-029 gen_all_queries seed=1 n=10000 m=200000 q=200000
