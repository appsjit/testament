class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        res = [[0 for c in range(n)] for r in range(m)]

        res[0][0] = grid[0][0]
        for r in range(1, m):  ## Initialize first column
            res[r][0] = res[r - 1][0] + grid[r][0]

        for c in range(1, n):  ## Initialize first row
            res[0][c] = res[0][c - 1] + grid[0][c]

        for r in range(1, m):
            for c in range(1, n):
                res[r][c] = min(res[r - 1][c], res[r][c - 1]) + grid[r][c]

        return res[m - 1][n - 1]