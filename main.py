
import squarify
import numpy as np
import pandas as pd
import votes as vos
from pywaffle import Waffle 
import matplotlib.pyplot as plt
from scipy.spatial import distance
from mpl_chord_diagram import chord_diagram
from sklearn.preprocessing import normalize
from scipy.spatial.distance import squareform
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import dendrogram, linkage
import constant as cst
import functions as fun

# https://pywaffle.readthedocs.io/en/latest/
# https://plotly.com/python/treemaps/
# https://www.mariowiki.com/Gallery:Mario_Kart_8

TRK_SET = set(cst.TRACKS)
COLORS = [
    '#2EB2FF', '#2837af', '#f00fbf', '#757aff', '#e30018',  
    '#45d40c', '#FCE900', '#92a0ab', '#F15062', '#ADE300', 
    '#FF9175', '#ffffff'
]
COLORS = [i+'95' for i in COLORS]
###############################################################################
# Load and validate votes 
###############################################################################
VOTES_RAW = {
    'April': vos.APRIL, 'Chip': vos.CHIP, 'Riché': vos.RICHIE, 
    'Yami': vos.YAMI, 'Alele': vos.ALELE, 'Chris': vos.CHRIS,
    'Tomás': vos.TOMAS, 'Amaya': vos.AMAYA, 'Mary': vos.MARY,
    'Memo': vos.MEMO, 'Leo': vos.LEO
}
(NAMES, VOTES) = (list(VOTES_RAW.keys()), list(VOTES_RAW.values()))
# Validate --------------------------------------------------------------------
valid = fun.validateEntries(VOTES, TRK_SET)
print('* Check for consistency:')
for (ix, i) in enumerate(valid):
    print('\t* {}: {}'.format(NAMES[ix], valid[ix]))
###############################################################################
# Collate Votes
###############################################################################
collated = [fun.flattenDictionary(fun.getVotesDictionary(i)) for i in VOTES]
votesDF = pd.DataFrame(collated, index=NAMES, columns=cst.TRACKS)
votesDF.loc['Total']= votesDF.sum()
votesDF.loc['Mean']= votesDF.mean()
votesDF.loc['Median']= votesDF.median()
votesDF.loc['SD']= votesDF.std()
votesDF.to_csv('./dta/votesDataframe.csv')
###############################################################################
# Plots
###############################################################################
MAX = fun.roundup(max(votesDF.loc['Total']))
print('* Plot:')
for track in cst.TRACKS:
    print('\t* {}\r'.format(track))
    votes = int(votesDF[track]['Total'])
    values = list(votesDF[track][NAMES])
    label = "{}: {} \n(μ: {:.2f}, M: {:.2f}, σ: {:.2f})\n".format(
        track, votes, 
        votesDF[track]['Mean'], votesDF[track]['Median'], votesDF[track]['SD']
    )
    fig = plt.figure( 
        values=values+[MAX-sum(values)], 
        labels=NAMES+[''],
        FigureClass=Waffle,
        colors=COLORS,
        vertical=False, columns=10, rows=5,
        block_arranging_style='new-line',
        block_aspect_ratio=1,
        rounding_rule='floor', starting_location='NW',
        title={
            'label': label,
            'loc': 'center', 
            'fontdict': {'fontsize': 20, 'color': '#000000'}
        },
        legend={
            'loc': 'lower left',
            'bbox_to_anchor': (0, -0.4),
            'ncol': 4, 'framealpha': 0, 'fontsize': 12
        }
    )
    fig.set_size_inches(10, 5)
    fig.ax.set_aspect(1)
    plt.axis('off')
    fig.savefig(
        './plt/WF_{}_{}.png'.format(str(votes).zfill(2), track), 
        dpi=500, bbox_inches='tight'
    )
    plt.close('all')
###############################################################################
# Euclidean Distance
###############################################################################
mat = []
for a in [np.asarray(votesDF.loc[nme].values) for nme in NAMES]:
    mat.append(
        [distance.euclidean(a, np.asarray(votesDF.loc[b].values)) for b in NAMES]
    )
mat = np.asarray(mat)
np.fill_diagonal(mat, 0)
matSca = np.asarray([np.interp(a, (min(i for i in a if i > 0), a.max()), (1, 0)) for a in mat])
matInv = np.asarray([np.interp(a, (min(i for i in a if i > 0), a.max()), (0, 1)) for a in mat])
np.fill_diagonal(matSca, 0)
np.fill_diagonal(matInv, 0)
###############################################################################
# Matrix
###############################################################################
(fig, ax) = plt.subplots()
ax.matshow(matSca, cmap='Purples', vmin=0, vmax=1.3)
for (i, j), z in np.ndenumerate(matSca):
    ax.text(j, i, '{:0.2f}'.format(z), ha='center', va='center')
ax.set_xticklabels(['']+NAMES)
ax.set_yticklabels(['']+NAMES)
fig.savefig(
    './plt/SM.png', 
    dpi=500, bbox_inches='tight'
)
plt.close('all')
###############################################################################
# Dendrogram
###############################################################################
(fig, ax) = plt.subplots()
dists = squareform(mat)
linkage_matrix = linkage(dists, "ward")
dend = dendrogram(linkage_matrix, labels=NAMES, color_threshold=0, orientation='right')
ax.set_aspect(.5)
plt.xticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
fig.savefig(
    './plt/DN.png', 
    dpi=500, bbox_inches='tight'
)
plt.close('all')
###############################################################################
# Chord Diagram
###############################################################################
(fig, ax) = plt.subplots()
chord_diagram(
    matSca, names=NAMES, colors=COLORS[:-1], alpha=.6,
    use_gradient=True, sorts='distance',
    order=[NAMES.index(i) for i in dend['ivl']]
)
plt.savefig(
    './plt/CH.png', 
    dpi=500, bbox_inches='tight'
)
plt.close('all')
