
import squarify
import numpy as np
import pandas as pd
import votes as vos
from pywaffle import Waffle 
import matplotlib.pyplot as plt 
from sklearn.metrics.pairwise import cosine_similarity
import constant as cst
import functions as fun

# https://pywaffle.readthedocs.io/en/latest/
# https://plotly.com/python/treemaps/

TRK_SET = set(cst.TRACKS)
COLORS = [
    '#2EB2FF', '#2837af', '#f00fbf', '#45d40c', '#e30018', '#FCE900'
]
###############################################################################
# Load and validate votes 
###############################################################################
VOTES_RAW = {
    'April': vos.APRIL, 'Chip': vos.CHIP, 'Riche': vos.RICHIE, 
    'Yami': vos.YAMI, 'Alele': vos.ALELE, 'Chris': vos.CHRIS
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
for track in cst.TRACKS:
    # (fig, ax) = plt.subplots(figsize=(10, 10))
    # Waffle ------------------------------------------------------------------
    votes = sum(votesDF[track])
    fig = plt.figure( 
        values=votesDF[track], labels=list(votesDF.index),
        FigureClass=Waffle,
        vertical=False, columns=10, 
        # rows=5,
        block_arranging_style='new-line',
        block_aspect_ratio=1,
        rounding_rule='floor',
        starting_location='NW',
        colors=COLORS,
        title={
            'label': "{}: {}\n".format(track, sum(votesDF[track])),
            'loc': 'center', 'fontdict': {'fontsize': 20}
        },
        legend={
            'loc': 'lower left',
            'bbox_to_anchor': (0, -0.4),
            'ncol': 10, #len(votesDF),
            'framealpha': 0,
            'fontsize': 12
        }
    )
    fig.set_size_inches(10, 5)
    fig.ax.set_aspect(1)
    plt.axis('off')
    fig.savefig(
        './plt/WF_{}_{}.png'.format(str(votes).zfill(2), track), 
        dpi=500, bbox_inches='tight'
    )
    # Treemap -----------------------------------------------------------------
    (fig, ax) = plt.subplots(figsize=(10, 10))
    sizes = list(votesDF[track])
    label = list(votesDF.index)
    votes = sum(votesDF[track])
    text = ['{}: {}'.format(*i) for i in zip(label, sizes)]
    ax = squarify.plot(
        sizes=sizes, # label=text, 
        alpha=1, color=COLORS,
        text_kwargs={'fontsize':12-5, 'color': "White"} #, 'fontweight': 'bold'}
    )
    plt.title(
        "{}: {}".format(track, votes), 
        fontsize=20, color="Black", fontweight='bold'
    )
    ax.set_aspect(.95)
    plt.axis('off')
    fig.savefig(
        './plt/TM_{}_{}.png'.format(str(votes).zfill(2), track), 
        dpi=500, bbox_inches='tight'
    )
    plt.close('all')
###############################################################################
# Add Stats
###############################################################################
votesDF.loc['Total']= votesDF.sum()
votesDF.loc['Mean']= votesDF.mean()
votesDF.to_csv('./dta/votesDataframe.csv')
###############################################################################
# Cosine Similarity
###############################################################################
a = np.asarray(votesDF.loc['Alele'].values)
b = np.asarray(votesDF.loc['Chip'].values)
cosine_similarity([a], [b])