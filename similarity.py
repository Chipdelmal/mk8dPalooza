

import numpy as np
from os import path
import pandas as pd
from random import shuffle
import constant as cst
import functions as fun


(PT_DTA, PT_PLT, FN_DTA) = (cst.PT_DTA, cst.PT_PLT, cst.FN_DTA)
(PLYRS, TRK_SET) = (cst.PLYRS, set(cst.TRACKS))
(DFUN, RAN) = (cst.DIST_FUN, cst.RANGE)
###############################################################################
# Read data and get constants
###############################################################################
VOTES_DF = pd.read_csv(path.join(PT_DTA, FN_DTA), index_col=0)
NAMES = list(PLYRS.keys())
if cst.ANONYMIZE:
    shuffle(NAMES)
###############################################################################
# Distance
###############################################################################
print('(2) Calculating Similarity Matrices')
distMat = fun.distanceMatrix(VOTES_DF, NAMES, distFun=DFUN)
distNrm = np.asarray([[i/sum(row) for i in row] for row in distMat])
distSca = np.asarray([
    np.interp(a, (min(i for i in a if i > 0), a.max()), RAN) for a in distNrm
])
np.fill_diagonal(distSca, 0)
###############################################################################
# Export
###############################################################################
np.savetxt(path.join(PT_DTA, cst.FN_DST), distMat, delimiter=',')
np.savetxt(path.join(PT_DTA, cst.FN_SCA), distSca, delimiter=',')
###############################################################################
# Final Stat (Winner is the closest to the total)
###############################################################################
stt = 'Median'
nmes = NAMES+[stt]
cpyDta = VOTES_DF.copy()
# cpyDta.loc[stt] = VOTES_DF.loc[stt]/len(NAMES)
distMat = fun.distanceMatrix(cpyDta, nmes, distFun=DFUN)
distNrm = np.asarray([[i/sum(row) for i in row] for row in distMat])
distSca = np.asarray([
    np.interp(a, (min(i for i in a if i > 0), a.max()), RAN) for a in distNrm
])
winner = {nmes[i]: distSca[-1][i] for i in range(len(nmes))}
srtd = dict(sorted(winner.items(), key=lambda item: item[1]))
srtd.pop(stt)
srtd
