class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])

        prep = [[0 for x in range(n)] for y in range(m)]
        ## Step 1 Sum horizontally
        for r in range(m):
            prep[r][0] = mat[r][0]  ## Copying Column 0 for all rows
            for c in range(1, n):
                prep[r][c] = prep[r][c - 1] + mat[r][c]  ## Sum up horizontally

        # Step2 on top of above sum vertically
        for c in range(n):
            for r in range(1, m):
                prep[r][c] = prep[r - 1][c] + prep[r][c]

        # Calculate
        for r in range(m):
            rUp = max(r - k, 0)
            rDown = min(r + k, m - 1)
            ##print('ru:'+str(ru)+'   rd:'+str(rd))
            for c in range(n):
                cLeft = max(c - k, 0)
                cRight = min(c + k, n - 1)
                value = prep[rDown][cRight]
                print(value)
                if (rUp - 1 >= 0):
                    value -= prep[rUp - 1][cRight]
                if (cLeft - 1 >= 0):
                    value -= prep[rDown][cLeft - 1]
                if (rUp - 1 >= 0 and cLeft - 1 >= 0):
                    value += prep[rUp - 1][cLeft - 1]
                mat[r][c] = value

        print(prep)
        return mat
