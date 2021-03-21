
import numpy as np
import pandas as pd
import votes as vos
import constant as cst
import functions as fun

TRK_SET = set(cst.TRACKS)
###############################################################################
# Load and validate votes 
###############################################################################
VOTES_RAW = {
    'April': vos.APRIL, 'Riche': vos.RICHIE, 'Chip': vos.CHIP
}
(NAMES, VOTES) = (list(VOTES_RAW.keys()), list(VOTES_RAW.values()))
# Validate --------------------------------------------------------------------
valid = fun.validateEntries(VOTES, TRK_SET)
for (ix, i) in enumerate(valid):
    print('* {}: {}'.format(NAMES[ix], valid[ix]))
###############################################################################
# Collate Votes
###############################################################################
collated = [fun.flattenDictionary(fun.getVotesDictionary(i)) for i in VOTES]
votesDF = pd.DataFrame(collated, index=NAMES, columns=cst.TRACKS)
votesDF.to_csv('./dta/votesDataframe.csv')