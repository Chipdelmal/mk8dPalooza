

import numpy as np
from os import path
import pandas as pd
from random import shuffle
from pywaffle import Waffle
import matplotlib.pyplot as plt
from mpl_chord_diagram import chord_diagram
from scipy.spatial.distance import squareform
import constant as cst
import functions as fun

import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap

(PT_DTA, PT_PLT, FN_DTA, FN_SCA, FN_DST) = (
    cst.PT_DTA, cst.PT_PLT, cst.FN_DTA, cst.FN_SCA, cst.FN_DST
)
(PLYRS, TRK_SET, RAN) = (cst.PLYRS, set(cst.TRACKS), cst.RANGE)
###############################################################################
# Read data and get constants
###############################################################################
VOTES_DF = pd.read_csv(path.join(PT_DTA, FN_DTA), index_col=0)
NAMES = list(PLYRS.keys())
COLORS = [PLYRS[i]['color'] for i in PLYRS.keys()]
COLORS = [(i + cst.ALPHA_HEX) for i in COLORS]
VOTES_RAW = {i: PLYRS[i]['votes'] for i in PLYRS.keys()}
(NAMES, VOTES) = (list(VOTES_RAW.keys()), list(VOTES_RAW.values()))
NAME_NUM = len(NAMES)
###############################################################################
# Load Matrix
###############################################################################
matRan = np.genfromtxt(path.join(PT_DTA, FN_SCA), delimiter=',')
if cst.ANONYMIZE:
    shuffle(NAMES)
    shuffle(COLORS)
###############################################################################
# Rank Matrix
###############################################################################
print('(3) Plotting Rank Matrix')
cmap = pl.cm.bwr_r
my_cmap = cmap(np.arange(cmap.N))
my_cmap[:,-1] = np.linspace(0, .7, cmap.N)
my_cmap = ListedColormap(my_cmap)
(fig, ax) = plt.subplots()
ax.matshow(matRan, cmap=my_cmap, vmin=-RAN[0]*1.25, vmax=RAN[0]*1.25)
for (i, j), z in np.ndenumerate(matRan):
    ax.text(j, i, '{}'.format(int(z)), ha='center', va='center', fontsize=7.5)
ax.set_xticks(np.arange(-1, NAME_NUM, 1))
ax.set_yticks(np.arange(-1, NAME_NUM, 1))
plt.xticks(rotation=90)
ax.set_xticklabels(['']+NAMES)
ax.set_yticklabels(['']+NAMES)
ax.set_xlim(-.5, NAME_NUM-.5)
ax.set_ylim(NAME_NUM-.5, -.5)
plt.title('Row-norm Similarity\n', fontdict={'size': 18})
for i in np.arange(.5, NAME_NUM, 1):
    plt.axhline(y=i, color='k', linestyle='-', lw=.5)
fig.savefig(
    path.join(PT_PLT, 'RM.png'), 
    dpi=500, bbox_inches='tight', facecolor='w'
)
plt.close('all')
###############################################################################
# Load Matrix
###############################################################################
matRan = np.genfromtxt(path.join(PT_DTA, FN_DST), delimiter=',')
if cst.ANONYMIZE:
    shuffle(NAMES)
    shuffle(COLORS)
###############################################################################
# Similarity Matrix
###############################################################################
print('(4) Plotting Distance Matrix')
cmap = cst.CMAPS[3]
my_cmap = cmap(np.arange(cmap.N))
my_cmap[:,-1] = np.linspace(0, .75, cmap.N)
my_cmap = ListedColormap(my_cmap)
(fig, ax) = plt.subplots()
ax.matshow(matRan, cmap=my_cmap, vmin=0, vmax=.3)
for (i, j), z in np.ndenumerate(matRan):
    ax.text(
        j, i, '{:.3f}'.format(z), 
        ha='center', va='center', fontsize=5,
        rotation=45
    )
ax.set_xticks(np.arange(-1, NAME_NUM, 1))
ax.set_yticks(np.arange(-1, NAME_NUM, 1))
plt.xticks(rotation=90)
ax.set_xticklabels(['']+NAMES)
ax.set_yticklabels(['']+NAMES)
ax.set_xlim(-.5, NAME_NUM-.5)
ax.set_ylim(NAME_NUM-.5, -.5)
plt.title('Distance Matrix\n', fontdict={'size': 18})
fig.savefig(
    path.join(PT_PLT, 'SM.png'), 
    dpi=500, bbox_inches='tight', facecolor='w'
)
plt.close('all')