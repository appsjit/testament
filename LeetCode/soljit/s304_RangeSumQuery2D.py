class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prep = [[0 for x in range(n)] for y in range(m)]

        for r in range(m):
            self.prep[r][0] = matrix[r][0]
            for c in range(1, n):
                self.prep[r][c] = self.prep[r][c - 1] + matrix[r][c]

        for c in range(n):
            for r in range(1, m):
                self.prep[r][c] = self.prep[r - 1][c] + self.prep[r][c]
        print(self.prep)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        value = self.prep[row2][col2]
        if (row1 - 1 >= 0):
            value -= self.prep[row1 - 1][col2]
        if (col1 - 1 >= 0):
            value -= self.prep[row2][col1 - 1]
        if (row1 - 1 >= 0 and col1 - 1 >= 0):
            value += self.prep[row1 - 1][col1 - 1]
        return value
        ##return self.prep[row2][col2] - self.prep[row1-1][col2] - self.prep[row2][col1 - 1] + self.prep[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# Following 1314 Matrix Block Sum