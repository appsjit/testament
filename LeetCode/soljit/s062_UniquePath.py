class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = 0

        grid = [[1]*m]*n

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return (grid[n-1][m-1])
