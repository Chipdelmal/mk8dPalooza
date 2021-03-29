
import math
import matplotlib
import numpy as np
from scipy.spatial import distance
from matplotlib.colors import LinearSegmentedColormap


def flattenList(newlist):
    return [item for items in newlist for item in items]


def countDiffsWithPool(votes, TRK_SET):
    return [len(TRK_SET - set(flattenList(i))) for i in votes]


def countTiersVotes(votes):
    return [set([len(i) for i in j]) for j in votes]


def flattenDictionary(dictionary):
    flattened = {}
    for tier in dictionary:
        for i in tier:
            flattened[i] = tier[i]
    return flattened


def getVotesDictionary(vote):
    num = len(vote)-1
    voteDict = [{i: 1+num-jx for i in j} for (jx, j) in enumerate(vote)]
    return voteDict


def validateEntries(votes, TRK_SET):
    lens = countTiersVotes(votes)
    diffs = countDiffsWithPool(votes, TRK_SET)
    vPairs = zip(lens, diffs)
    valid = [True if (len(x[0]) == 1 and x[1] == 0) else False for x in vPairs]
    return valid

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


def distanceMatrix(votesDF, names, distFun=distance.euclidean, diagFill=0):
    mat = []
    for a in [np.asarray(votesDF.loc[nme].values) for nme in names]:
        mat.append([
            distFun(a, np.asarray(votesDF.loc[b].values)) for b in names
        ])
    mat = np.asarray(mat)
    np.fill_diagonal(mat, diagFill)
    return mat


def addHexOpacity(colors, alpha='1A'):
    return [c+alpha for c in colors]


def replaceHexOpacity(colors, alpha='FF'):
    return [i[:-2]+alpha for i in colors]


def generateAlphaColorMapFromColor(
    color
):
    alphaMap = LinearSegmentedColormap.from_list(
        'tempMap',
        [(0.0, 0.0, 0.0, 0.0), color],
        gamma=0
    )
    return alphaMap


def generateAlphaColorMapFromColorArray(
    colorArray
):
    elementsNumb = len(colorArray)
    cmapsList = [None] * elementsNumb
    for i in range(0, elementsNumb):
        cmapsList[i] = generateAlphaColorMapFromColor(colorArray[i])
    return cmapsList
