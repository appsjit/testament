class Solution:
    def calcDist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        leNuts = len(nuts)

        res = 0
        saving = -inf
        for z in range(leNuts):
            distFroms1 = self.calcDist(squirrel, nuts[z])
            distFromTr = self.calcDist(tree, nuts[z])

            res += distFromTr * 2
            ## check for nut where (tree to nut and back) minus (sq to nut to tree) is maximum. So that that nut can be chosen as the first one
            saving = max(2 * distFromTr - (distFroms1 + distFromTr), saving)

        return res - saving




