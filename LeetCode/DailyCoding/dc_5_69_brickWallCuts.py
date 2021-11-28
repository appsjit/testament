from collections import defaultdict
def lesserCuts(wall):
    myDict = defaultdict(int)
    rows = len(wall)
    for r in wall:
        brLen = 0
        for brick in r[:-1]: ##  Not considering last brick
            brLen += brick
            myDict[brLen] += 1

    return rows - max(myDict.values())


w = [[3,5,1,1],
     [2,3,3,2],
     [5,5],
     [4,4,2],
     [1,3,3,3],
     [1,1,6,1,1]]


print(lesserCuts(w))

