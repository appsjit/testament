import math
class Solution:
    def luckyNumbers(self, matrix):## List[List[int]]) -> List[int]:
        maxNum = math.inf
        r = len(matrix)
        c = len(matrix[0])

        minRow = []
        maxRow = []
        maxCol = []
        luckyNum = -math.inf
        ans = []
        min
        for i in range(0, r):
            curMin = maxNum
            # for j in range(0, c):
            #     curMin = min(matrix[i][j], curMin)
            minRow.append(min(matrix[i]))
            maxRow.append(max(matrix[i]))
        ##    luckyNum = max(luckyNum, curMin)
        print(minRow)


        for j in range(0, c):
            curMaxCol = -math.inf
            for i in range(0, r):
                curMaxCol = max(curMaxCol, matrix[i][j])
            maxCol.append(curMaxCol)

        print(maxCol)

        for x in minRow:
            if x in maxCol:
                ans.append(x)
        return ans

s = Solution();
matrix = [[36376,85652,21002,4510],[68246,64237,42962,9974],[32768,97721,47338,5841],[55103,18179,79062,46542]]
##matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(s.luckyNumbers(matrix))