class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        ##  1   2   3
        ##  4   5   6
        ##  7   8   9

        ##  1   2   3
        ## Minimum from first Line is 1
        ##  6   6   7
        ##  For first column on second row minimum would be second row first column + minimum from first row except column 1
        ##  13  14  15

        r = len(grid)
        c = len(grid[0])

        for i in range(1, r):
            lastRowMin = min(grid[i - 1])
            ## Minimum from first Line is 1
            lastMinIdx = grid[i - 1].index(lastRowMin)
            ##  For 1st col on 2nd row min would be 2nd row 1st col + min from 1st row except Col 1
            lastRowNextMin = min(v for k, v in enumerate(grid[i - 1]) if k != lastMinIdx)

            print(str(lastRowMin) + '     ' + str(lastMinIdx) + '     ' + str(lastRowNextMin))
            for j in range(c):
                if grid[i - 1][j] == lastRowMin:
                    ##  For 1st col on 2nd row min would be 2nd row 1st col + min from 1st row except Col 1
                    grid[i][j] += lastRowNextMin
                else:  ## Minimum from first Line is 1
                    grid[i][j] += lastRowMin

        return min(grid[-1])