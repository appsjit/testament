class Solution:
    def processNeighbors(self, pi, pj):
        if (pi < 0 or pj < 0 or pi >= self.r or pj >= self.c or updGrid[pi][pj] != '1'):
            return

        updGrid[pi][pj] = 0
        self.processNeighbors(pi - 1, pj)
        self.processNeighbors(pi + 1, pj)
        self.processNeighbors(pi, pj - 1)
        self.processNeighbors(pi, pj + 1)

    def numIslands(self, grid: List[List[str]]) -> int:

        global updGrid
        updGrid = grid
        self.r = len(grid)
        self.c = len(grid[0])
        ans = 0
        for i in range(0, self.r):
            for j in range(0, self.c):
                if updGrid[i][j] == '1':
                    ans += 1
                    self.processNeighbors(i, j)

        return ans

