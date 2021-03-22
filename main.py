
import squarify
import numpy as np
import pandas as pd
import votes as vos
from pywaffle import Waffle 
import matplotlib.pyplot as plt
from scipy.spatial import distance
from sklearn.preprocessing import normalize
from scipy.spatial.distance import squareform
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import dendrogram, linkage
import constant as cst
import functions as fun

# https://pywaffle.readthedocs.io/en/latest/
# https://plotly.com/python/treemaps/

TRK_SET = set(cst.TRACKS)
COLORS = [
    '#2EB2FF', '#2837af', '#f00fbf', '#757aff', '#e30018',  '#45d40c',
    '#FCE900', '#ffffff'
]
MAX = 50
COLORS = [i+'95' for i in COLORS]
###############################################################################
# Load and validate votes 
###############################################################################
VOTES_RAW = {
    'April': vos.APRIL, 'Chip': vos.CHIP, 'Riché': vos.RICHIE, 
    'Yami': vos.YAMI, 'Alele': vos.ALELE, 'Chris': vos.CHRIS,
    'Tomás': vos.TOMAS
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
    values = list(votesDF[track])
    values.append(MAX-votes)
    labels=list(votesDF.index)
    labels.append('Padding')
    fig = plt.figure( 
        values=values, labels=labels,
        FigureClass=Waffle,
        vertical=False, columns=10, 
        rows=5,
        block_arranging_style='new-line',
        block_aspect_ratio=1,
        rounding_rule='floor',
        starting_location='NW',
        colors=COLORS,
        title={
            'label': "{}: {}\n".format(track, sum(votesDF[track])),
            'loc': 'center', 
            'fontdict': {'fontsize': 20, 'color': '#000000'}
        },
        legend={
            'loc': 'lower left',
            'bbox_to_anchor': (0, -0.4),
            'ncol': 4, #len(votesDF),
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
    plt.close('all')
    # Treemap -----------------------------------------------------------------
    # (fig, ax) = plt.subplots(figsize=(10, 10))
    # sizes = list(votesDF[track])
    # label = list(votesDF.index)
    # votes = sum(votesDF[track])
    # text = ['{}: {}'.format(*i) for i in zip(label, sizes)]
    # ax = squarify.plot(
    #     sizes=sizes, # label=text, 
    #     alpha=.9, color=COLORS, pad=.1
    #     text_kwargs={'fontsize':12-5, 'color': "White"} #, 'fontweight': 'bold'}
    # )
    # plt.title(
    #     "{}: {}".format(track, votes), 
    #     fontsize=20, color="Black", fontweight='bold'
    # )
    # ax.set_aspect(.95)
    # plt.axis('off')
    # fig.savefig(
    #     './plt/TM_{}_{}.png'.format(str(votes).zfill(2), track), 
    #     dpi=500, bbox_inches='tight'
    # )
    # plt.close('all')
###############################################################################
# Add Stats
###############################################################################
votesDF.loc['Total']= votesDF.sum()
votesDF.loc['Mean']= votesDF.mean()
votesDF.to_csv('./dta/votesDataframe.csv')
###############################################################################
# Cosine Similarity
###############################################################################
mat = []
for a in [np.asarray(votesDF.loc[nme].values) for nme in NAMES]:
    mat.append(
        [cosine_similarity([a], [np.asarray(votesDF.loc[b].values)])[0][0] for b in NAMES]
    )
mat = np.asarray(mat)
np.fill_diagonal(mat, 0)
# nrm = np.asarray([[i/np.sum(row) for i in row] for row in mat])

scaler = MinMaxScaler(feature_range=(0, 100))
scaler.fit_transform(mat)

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
fig, ax = plt.subplots()
ax.matshow(mat, cmap='seismic', vmin=10, vmax=30)
for (i, j), z in np.ndenumerate(mat):
    ax.text(j, i, '{:0.1f}'.format(z), ha='center', va='center')
ax.set_xticklabels(['']+NAMES)
ax.set_yticklabels(['']+NAMES)
fig.savefig(
    './plt/SM.png', 
    dpi=500, bbox_inches='tight'
)
dists = squareform(mat)
linkage_matrix = linkage(dists, "single")
dendrogram(linkage_matrix, labels=NAMES, color_threshold=0)
plt.show()