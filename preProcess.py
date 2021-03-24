

import pandas as pd
from os import path
import votes as vos
import constant as cst
import functions as fun


PT_OUT = './dta/'
TRK_SET = set(cst.TRACKS)
###############################################################################
# Load and validate votes 
###############################################################################
VOTES_RAW = {
    'Alele': vos.ALELE, 'Amaya': vos.AMAYA, 'April': vos.APRIL, 
    'Chip': vos.CHIP, 'Chris': vos.CHRIS, 'Leo': vos.LEO, 
    'Mary': vos.MARY, 'Memo': vos.MEMO, 'Riché': vos.RICHIE, 
    'Tomás': vos.TOMAS, 'Yami': vos.YAMI  
}
(NAMES, VOTES) = (list(VOTES_RAW.keys()), list(VOTES_RAW.values()))
# Validate --------------------------------------------------------------------
valid = fun.validateEntries(VOTES, TRK_SET)
print('(1) Check for consistency:')
for (ix, i) in enumerate(valid):
    print('\t- {}: {}'.format(NAMES[ix], valid[ix]))
# Print validation ------------------------------------------------------------
if all(valid):
    print('\t* [All entries are valid]')
else:
    print('\t* [Some entries contain errors!]')
###############################################################################
# Collate Votes
###############################################################################
collated = [fun.flattenDictionary(fun.getVotesDictionary(i)) for i in VOTES]
votesDF = pd.DataFrame(collated, index=NAMES, columns=cst.TRACKS)
votesDF.loc['Total']= votesDF.sum()
votesDF.loc['Mean']= votesDF.mean()
votesDF.loc['Median']= votesDF.median()
votesDF.loc['SD']= votesDF.std()
votesDF.to_csv(path.join(PT_OUT, 'votesDataframe.csv'))