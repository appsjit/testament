class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        for i in range(1, r):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)

        # Filling the values for the first row
        for j in range(1, c):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)

        for i in range(1, r):
            for j in range(1, c):
                if (obstacleGrid[i][j]) == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0

        print(obstacleGrid)
        return obstacleGrid[r - 1][c - 1]
