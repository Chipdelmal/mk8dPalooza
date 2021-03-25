
import numpy as np
from os import path
import pandas as pd
from pywaffle import Waffle
import matplotlib.pyplot as plt
from mpl_chord_diagram import chord_diagram
from scipy.spatial.distance import squareform
import constant as cst
import functions as fun

import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap

(PT_DTA, PT_PLT, FN_DTA, FN_SCA) = (
    cst.PT_DTA, cst.PT_PLT, cst.FN_DTA, cst.FN_SCA
)
(PLYRS, TRK_SET) = (cst.PLYRS, set(cst.TRACKS))
###############################################################################
# Read data and get constants
###############################################################################
VOTES_DF = pd.read_csv(path.join(PT_DTA, FN_DTA), index_col=0)
NAMES = list(PLYRS.keys())
COLORS = [PLYRS[i]['color'] for i in PLYRS.keys()]
COLORS = [(i + cst.ALPHA_HEX) for i in COLORS]
###############################################################################
# Load Matrix
###############################################################################
VOTES_RAW = {i: PLYRS[i]['votes'] for i in PLYRS.keys()}
(NAMES, VOTES) = (list(VOTES_RAW.keys()), list(VOTES_RAW.values()))
matRan = np.genfromtxt(path.join(PT_DTA, FN_SCA), delimiter=',')
###############################################################################
# Matrix
###############################################################################
print('(3) Plotting Similarty Matrix')
cmap = pl.cm.Blues
my_cmap = cmap(np.arange(cmap.N))
my_cmap[:,-1] = np.linspace(0, .7, cmap.N)
my_cmap = ListedColormap(my_cmap)
(fig, ax) = plt.subplots()
ax.matshow(matRan, cmap=my_cmap, vmin=0, vmax=100)
for (i, j), z in np.ndenumerate(matRan):
    ax.text(j, i, '{}'.format(int(z)), ha='center', va='center', fontsize=7.5)
ax.set_xticks(np.arange(-1, 11, 1))
ax.set_yticks(np.arange(-1, 11, 1))
plt.xticks(rotation=90)
ax.set_xticklabels(['']+NAMES)
ax.set_yticklabels(['']+NAMES)
ax.set_xlim(-.5, 10.5)
ax.set_ylim(10.5, -.5)
fig.savefig(
    path.join(PT_PLT, 'SM.png'), 
    dpi=500, bbox_inches='tight'
)
plt.close('all')