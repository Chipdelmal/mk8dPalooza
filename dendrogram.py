
import numpy as np
from os import path
from random import shuffle
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import dendrogram, linkage, set_link_color_palette
import constant as cst
import functions as fun


(PT_DTA, PT_PLT, FN_DTA, FN_DST) = (
    cst.PT_DTA, cst.PT_PLT, cst.FN_DTA, cst.FN_DST
)
(PLYRS, TRK_SET) = (cst.PLYRS, set(cst.TRACKS))
###############################################################################
# Load Matrix
###############################################################################
VOTES_RAW = {i: PLYRS[i]['votes'] for i in PLYRS.keys()}
(NAMES, VOTES) = (list(VOTES_RAW.keys()), list(VOTES_RAW.values()))
mat = np.genfromtxt(path.join(PT_DTA, FN_DST), delimiter=',')
if cst.ANONYMIZE:
    shuffle(NAMES)
###############################################################################
# Process
###############################################################################
print('(5) Plotting Dendrogram')
dists = squareform(mat)
linkage_matrix = linkage(dists, 'ward')
###############################################################################
# Plot
###############################################################################
(fig, ax) = plt.subplots()
set_link_color_palette(['#ff006e', '#2614ed', 'k'])
dend = dendrogram(
    linkage_matrix, 
    labels=NAMES, orientation='right',
    above_threshold_color='#bcbddcA0', 
    count_sort='descending'
)
ax.set_aspect(.0025)
plt.xticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_color('#ffffff')
plt.title('Hierarchical Clustering\n', fontdict={'size': 18})
fig.savefig(
    path.join(PT_PLT, 'DN.png'), 
    dpi=500, bbox_inches='tight', facecolor='w'
)
plt.close('all')