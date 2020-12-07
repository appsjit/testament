class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        print(matrix)

        if not matrix or not matrix[0]:
            return []
        r = len(matrix)
        c = len(matrix[0])
        ans = []
        i, j = 0, 0
        direction = 1  ##1 if coming up
        while i < r and j < c:
            ans.append(matrix[i][j])
            ##print(matrix[i][j])

            ni = i - direction
            nj = j + direction

            if (ni < 0 or ni == r or nj < 0 or nj == c):
                if direction > 0:  ## traversing up and reached top/right
                    if (j == c - 1):  ## if reached right most
                        i += 1  ##(j == c -1)
                    j += (j < c - 1)  ## if within boundary
                else:
                    if (i == r - 1):  ## if reached bottom
                        j += 1
                    i += (i < r - 1)  ## if within boundary

                direction = -1 * direction
            else:
                i = ni
                j = nj

        return ans






