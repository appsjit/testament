class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        oneExists = False

        for r in range(m):
            for c in range(n):
                if int(matrix[r][c]) > 0:
                    oneExists = True

                    ## Minimum of earlier 3 quadrants + 1
        for r in range(1, m):
            for c in range(1, n):
                if (int(matrix[r - 1][c]) > 0 and int(matrix[r][c - 1]) > 0 and int(matrix[r - 1][c - 1]) > 0 and int(
                        matrix[r][c]) > 0):
                    matrix[r][c] = min(int(matrix[r - 1][c]), int(matrix[r][c - 1]), int(matrix[r - 1][c - 1])) + 1
                    ans = max(ans, matrix[r][c])

        if (ans == 0 and oneExists == True):
            return 1
        return ans * ans

