class Solution:
    memo = defaultdict(int)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        r = len(matrix)
        c = len(matrix[0])

        def validNeighbor(i, j):
            n = []
            if (i > 0):
                n.append((i - 1, j))
            if (i < r - 1):
                n.append((i + 1, j))
            if (j > 0):
                n.append((i, j - 1))
            if (j < c - 1):
                n.append((i, j + 1))
            return n

        @lru_cache(None)
        def pathFinder(pi, pj):
            longest_path = []

            for i, j in validNeighbor(pi, pj):
                if (matrix[pi][pj] > matrix[i][j]):
                    longest_path.append(pathFinder(i, j) + 1)
            return max(longest_path) if longest_path else 1

        ans = []
        for i in range(0, r):
            for j in range(0, c):
                ans.append(pathFinder(i, j))

        return max(ans)

    # class Solution:
#     memo = defaultdict(int)
#     def validNeighbor(self, pi, pj, pr, pc):
#         if (pi > -1 and pi < pr and pj > -1 and pj < pc ):
#             return True
#         return False

#     def getLongSeq(self, pCurCell, pVal, pParhF):
#         if (pCurCell not in pParhF.keys()):
#             ##print('Not Found:'+str(pCurCell))
#             pVal += 1
#             return pVal
#         if pCurCell in self.memo.keys():
#             return self.memo[pCurCell]
#         nextBranches = pParhF[pCurCell]
#         ##print(str(pCurCell)+'  its dir branch  '+str(nextBranches))
#         retVal = 0
#         for nextCell in nextBranches:
#             retVal = max(retVal, self.getLongSeq(nextCell, pVal, pParhF))
#         self.memo[pCurCell] = pVal + retVal
#         return self.memo[pCurCell] ##pVal + retVal
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         if not matrix:
#             return 0
#         r = len(matrix)
#         c = len(matrix[0])
#         pathFinder = defaultdict(list)
#         for i in range(0, r):
#             for j in range(0, c):
#                 curVal = matrix[i][j]
#                 ##print(str(matrix[i][j])+'   '+str(i)+'   '+str(j))
#                 if (self.validNeighbor(i+1, j, r, c) and matrix[i+1][j] > curVal) :
#                     validNbr = (i+1,j)
#                     pathFinder[(i,j)].append(validNbr)
#                 if (self.validNeighbor(i, j+1, r, c) and matrix[i][j+1] > curVal) :
#                     validNbr = (i,j+1)
#                     pathFinder[(i,j)].append(validNbr)
#                 if (self.validNeighbor(i-1, j, r, c) and matrix[i-1][j] > curVal) :
#                     validNbr = (i-1,j)
#                     pathFinder[(i,j)].append(validNbr)
#                 if (self.validNeighbor(i, j-1, r, c) and matrix[i][j-1] > curVal) :
#                     validNbr = (i,j-1)
#                     pathFinder[(i,j)].append(validNbr)
#         res = 0
#         for k, v in pathFinder.items():
#             ##print(str(k)+'   '+str(v))
#             lval = self.getLongSeq(k, 1, pathFinder)
#             ##print(lval)
#             res = max(res, lval -1)

#         return res if res > 1 else 1


