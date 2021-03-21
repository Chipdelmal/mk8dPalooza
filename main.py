
import numpy as np
import pandas as pd
import votes as vos
import matplotlib.pyplot as plt 
from pywaffle import Waffle 
import constant as cst
import functions as fun
import squarify 
# https://pywaffle.readthedocs.io/en/latest/

TRK_SET = set(cst.TRACKS)
###############################################################################
# Load and validate votes 
###############################################################################
VOTES_RAW = {
    'April': vos.APRIL, 'Chip': vos.CHIP,
    'Riche': vos.RICHIE, 'Yami': vos.YAMI
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
###############################################################################
# Plots
###############################################################################
track = cst.TRACKS[-1]
# Waffle ----------------------------------------------------------------------
(fig, ax) = plt.subplots()
plt.figure( 
    values=votesDF[track], labels=list(votesDF.index),
    FigureClass=Waffle,
    vertical=False, columns=8, 
    rows=5,
    # block_arranging_style='new-line',
    block_aspect_ratio=1,
    rounding_rule='floor',
    starting_location='NW',
    colors=[
        '#22a5f1', '#ff006e', '#45d40c', '#8338ec'
    ],
    title={
        'label': "{}: {}\n".format(track, sum(votesDF[track])),
        'loc': 'center', 'fontdict': {'fontsize': 20}
    },
    legend={
        'loc': 'lower left',
        'bbox_to_anchor': (0, -0.4),
        'ncol': len(votesDF),
        'framealpha': 0,
        'fontsize': 12
    }
)
ax.set_aspect(1)
plt.axis('off')
plt.show()
# Treemap ---------------------------------------------------------------------
(fig, ax) = plt.subplots()
sizes=list(votesDF[track])
label=list(votesDF.index)
squarify.plot(
    sizes=sizes, label=label, 
    alpha=0.95, color=[
        '#22a5f1', '#ff006e', '#45d40c', '#8338ec'
    ],
    text_kwargs={'fontsize':15, 'color': "White", 'fontweight': 'bold'}
)
plt.title(
    "{}: {}".format(track, sum(votesDF[track])), 
    fontsize=17.5, color="Black"
)
ax.set_aspect(.95)
plt.axis('off')
plt.show()
###############################################################################
# Add Stats
###############################################################################
votesDF.loc['Total']= votesDF.sum()
votesDF.loc['Mean']= votesDF.mean()
votesDF.to_csv('./dta/votesDataframe.csv')