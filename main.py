
import numpy as np
import pandas as pd
import votes as vos
import constant as cst
import functions as fun

TRK_SET = set(cst.TRACKS)
###############################################################################
# Load and validate votes 
###############################################################################
VOTES = [vos.APRIL]
# Validate --------------------------------------------------------------------
lens = [set([len(i) for i in j]) for j in VOTES]
diffs = [len(TRK_SET - set(fun.flattenList(i))) for i in VOTES]
for (ix, i) in enumerate(zip(lens, diffs)):
    print('* [{}] Len: {}, Diff: {}'.format(ix, *i))