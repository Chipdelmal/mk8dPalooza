
# https://plotly.com/python/treemaps/

from os import path
import pandas as pd
from random import shuffle
from pywaffle import Waffle
import matplotlib.pyplot as plt
import constant as cst
import functions as fun


(PT_DTA, PT_PLT, FN_DTA) = (cst.PT_DTA, cst.PT_PLT, cst.FN_DTA)
(PLYRS, TRK_SET, LEGEND) = (cst.PLYRS, set(cst.TRACKS), cst.WF_LEGEND)
###############################################################################
# Read data and get constants
###############################################################################
VOTES_DF = pd.read_csv(path.join(PT_DTA, FN_DTA), index_col=0)
NAMES = list(PLYRS.keys())
COLORS = [PLYRS[i]['color'] for i in PLYRS.keys()]
COLORS = [(i + cst.ALPHA_HEX) for i in COLORS]
MAX = fun.roundup(max(VOTES_DF.loc['Total']))
SORTING = [int(i) for i in sorted(VOTES_DF.loc['Total'])][::-1]
TRACKS = cst.TRACKS
if cst.ANONYMIZE:
    shuffle(NAMES)
    shuffle(COLORS)
    shuffle(TRACKS)
###############################################################################
# Plots
###############################################################################
print('(7) Plotting Waffles')
for (ix, track) in enumerate(TRACKS):
    print('\t* {}{}'.format(track, ' '*10), end='\r')
    votes = int(VOTES_DF[track]['Total'])
    values = list(VOTES_DF[track][NAMES])
    tSize = 27.5
    if LEGEND:
        tSize = 22.5
    if cst.PRINT_STATS:
        label = '{}. {} ({}) \n(μ: {:.2f}, M: {:.2f}, σ: {:.2f})\n'.format(
            str(len(TRK_SET)-(ix+1)).zfill(2), 
            track, votes, 
            VOTES_DF[track]['Mean'], 
            VOTES_DF[track]['Median'], 
            VOTES_DF[track]['SD']
        )
    else:
        label = "{} ({}) {}: {}\n".format(
            str(SORTING.index(votes)+1).zfill(2), 
            SORTING.count(votes),
            track, votes
        )
    fig = plt.figure( 
        values=values+[MAX-sum(values)], 
        labels=NAMES + [cst.VOID[0]],
        colors=COLORS + [cst.VOID[1]],
        FigureClass=Waffle,
        vertical=False, rows=10,
        block_arranging_style='normal', block_aspect_ratio=2,
        starting_location='NW',
        title={
            'label': label, 'loc': 'center', 
            'fontdict': {'fontsize': tSize, 'color': '#000000'}
        },
        legend={
            # 'loc': 'upper right', 'bbox_to_anchor': (0, 0), 'mode': "expand",
            'bbox_to_anchor': (1.05, 1), 'loc': 'upper left', 'borderaxespad': 0,
            'ncol': 1, 'framealpha': 0, 'fontsize': 12, 'labelcolor':'#000000'
        }
    )
    fig.set_size_inches(10, 5)
    fig.ax.set_aspect(1)
    plt.axis('off')
    prep = 'LBL_'
    if not LEGEND:
        plt.gca().get_legend().remove()
        prep = ''
    fig.savefig(
        path.join(
            PT_PLT, prep+'WF_{}_{}.png'.format(str(votes).zfill(2), track)
        ), 
        dpi=500, facecolor='w', bbox_inches='tight', pad_inches=0.2
    )
    plt.close('all')

