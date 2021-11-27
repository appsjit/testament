class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ## Min heap
        ## Using min on each row

        # 2
        # 5   6
        # 11  10  13
        # 15  11  18  16

        r = len(triangle)

        ans = triangle[0][0]

        i = 0
        prevRow = triangle[0]
        for row in range(1, r):
            curRow = []
            for c in range(row + 1):
                prevRowColMin = float(inf)
                if c > 0:
                    prevRowColMin = prevRow[c - 1]
                if c < row:
                    prevRowColMin = min(prevRowColMin, prevRow[c])

                curRow.append(triangle[row][c] + prevRowColMin)

                print(triangle[row][c])
            prevRow = curRow
            print(prevRow)
            # minRowVal = min(triangle[row][i], triangle[row][i+1])
            # i = triangle[row].index(minRowVal)
            # ans += minRowVal

        return min(prevRow)


