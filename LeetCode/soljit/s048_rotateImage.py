class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        # transpose matrix
        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        #     matrix[i] = matrix[i][::-1]

        ## Using Side Rotates
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                print(tmp)
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = matrix[i][j]
                matrix[i][j] = tmp

        ##print(matrix)