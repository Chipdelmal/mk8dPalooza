
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
COLORS = [
    '#22a5f1', '#2837af', '#f00fbf', '#45d40c'
]
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
track = cst.TRACKS[2]
# (fig, ax) = plt.subplots(figsize=(10, 10))
# Waffle ----------------------------------------------------------------------
fig = plt.figure( 
    values=votesDF[track], labels=list(votesDF.index),
    FigureClass=Waffle,
    vertical=False, columns=8, 
    rows=5,
    # block_arranging_style='new-line',
    block_aspect_ratio=1,
    rounding_rule='floor',
    starting_location='NW',
    colors=COLORS,
    # title={
    #     'label': "{}: {}\n".format(track, sum(votesDF[track])),
    #     'loc': 'center', 'fontdict': {'fontsize': 20}
    # },
    legend={
        'loc': 'lower left',
        'bbox_to_anchor': (0, -0.4),
        'ncol': 2, #len(votesDF),
        'framealpha': 0,
        'fontsize': 12
    }
)
fig.set_size_inches(5, 5)
fig.ax.set_aspect(1)
plt.axis('off')
fig.savefig('./plt/'+track+'_waffle.png', dpi=500)
# Treemap ---------------------------------------------------------------------
(fig, ax) = plt.subplots(figsize=(10, 10))
sizes=list(votesDF[track])
label=list(votesDF.index)
ax = squarify.plot(
    sizes=sizes, # label=label, 
    alpha=0.95, color=COLORS,
    # text_kwargs={'fontsize':15, 'color': "White"} #, 'fontweight': 'bold'}
)
plt.title(
    "{}: {}".format(track, sum(votesDF[track])), 
    fontsize=20, color="Black" # , fontweight='bold'
)
ax.set_aspect(.95)
plt.axis('off')
plt.show()
fig.savefig('./plt/'+track+'_treemap.png', dpi=500)
###############################################################################
# Add Stats
###############################################################################
votesDF.loc['Total']= votesDF.sum()
votesDF.loc['Mean']= votesDF.mean()
votesDF.to_csv('./dta/votesDataframe.csv')