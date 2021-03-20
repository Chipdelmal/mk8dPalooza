
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