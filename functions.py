
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
    vote.reverse()
    voteDict = [{i: jx for i in j} for (jx, j) in enumerate(vote)]
    return voteDict


def validateEntries(votes, TRK_SET):
    lens = countTiersVotes(votes)
    diffs = countDiffsWithPool(votes, TRK_SET)
    vPairs = zip(lens, diffs)
    valid = [True if (len(x[0]) == 1 and x[1] == 0) else False for x in vPairs]
    return valid