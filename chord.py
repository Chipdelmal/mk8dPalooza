
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
if cst.ANONYMIZE:
    shuffle(NAMES)
    shuffle(COLORS)
###############################################################################
# Chord Diagram
###############################################################################
print('(6) Plotting Chord Diagram')
(fig, ax) = plt.subplots()
chord_diagram(
    matRan, names=NAMES, colors=COLORS, alpha=.6,
    use_gradient=True, width=0.1, chordwidth=.4
    # order=[NAMES.index(i) for i in NAMES]
    # sorts='distance'
)
plt.savefig(
    path.join(PT_PLT, 'CH.png'),
    dpi=500, bbox_inches='tight'
)
plt.close('all')
