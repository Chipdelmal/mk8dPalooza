
import numpy as np
import pandas as pd
import votes as vos
import constant as cst
import functions as fun

TRK_SET = set(cst.TRACKS)
###############################################################################
# Load and validate votes 
###############################################################################
VOTES_RAW = {'April': vos.APRIL}
VOTES = list(VOTES_RAW.values())
# Validate --------------------------------------------------------------------
lens = fun.countTiersVotes(VOTES)
diffs = fun.countDiffsWithPool(VOTES, TRK_SET)
for (ix, i) in enumerate(zip(lens, diffs)):
    print('* [{}] Len: {}, Diff: {}'.format(ix, *i))
###############################################################################
# Collate Votes
###############################################################################
collated = [fun.flattenDictionary(fun.getVotesDictionary(i)) for i in VOTES]
votesDF = pd.DataFrame(
    collated, 
    index=list(VOTES_RAW.keys()), 
    columns=cst.TRACKS
)