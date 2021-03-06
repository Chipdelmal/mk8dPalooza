

import pandas as pd
from os import path
import votes as vos
import constant as cst
import functions as fun


(PT_DTA, FN_DTA, FN_RSP) = (cst.PT_DTA, cst.FN_DTA, cst.FN_RSP)
(PLYRS, TRK_SET) = (cst.PLYRS, set(cst.TRACKS))
###############################################################################
# Load Votes 
###############################################################################
VOTES_RAW = {i: PLYRS[i]['votes'] for i in PLYRS.keys()}
(NAMES, VOTES) = (list(VOTES_RAW.keys()), list(VOTES_RAW.values()))
###############################################################################
# Validate 
###############################################################################
valid = fun.validateEntries(VOTES, TRK_SET)
msg = '(1) Checking for consistency'
# Print validation ------------------------------------------------------------
if all(valid):
    print('{} (all entries are valid)'.format(msg))
else:
    print('{} ({}  contains errors!)'.format(msg, NAMES[valid.index(False)]))
###############################################################################
# Collate
###############################################################################
collated = [fun.flattenDictionary(fun.getVotesDictionary(i)) for i in VOTES]
votesDF = pd.DataFrame(collated, index=NAMES, columns=cst.TRACKS)
votesDF.loc['Total']= votesDF.sum()
votesDF.loc['Mean']= votesDF.mean()
votesDF.loc['Median']= votesDF.median()
votesDF.loc['SD']= votesDF.std()
###############################################################################
# Re-shape to Flat DF
###############################################################################
df = votesDF
df['Name'] = list(votesDF.index.values.tolist())
mlt = pd.melt(votesDF, id_vars=['Name'], var_name='Track', value_name='Votes')
conds = zip(
    mlt['Name']!='SD', mlt['Name']!='Mean', 
    mlt['Name']!='Median', mlt['Name']!='Total'
)
fltr = [all(i) for i in conds]
reshapped = mlt[fltr]
###############################################################################
# Export
###############################################################################
votesDF = votesDF.drop(columns=['Name'])
votesDF.to_csv(path.join(PT_DTA, FN_DTA))
reshapped.to_csv(path.join(PT_DTA, FN_RSP), index=False)