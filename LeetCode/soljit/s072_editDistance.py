class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        r = len(word1)  # Source on Row
        c = len(word2)  # Target on Column

        if r * c == 0:
            return r + c

        # array to store the convertion history   row0, row1, row2 etc
        d = [[0] * (r + 1) for _ in range(c + 1)]

        ## Initialize Boundaries
        for x in range(c + 1):  ## . x for c
            d[x][0] = x

        for y in range(r + 1):  ##  y for r
            d[0][y] = y

        ## Iteration Order does not make diffrence
        for ri in range(1, r + 1):
            for ci in range(1, c + 1):

                # for ci in range(1, c+1):
                #     for ri in range(1, r+1):

                left = d[ci - 1][ri] + 1
                top = d[ci][ri - 1] + 1
                diag = d[ci - 1][ri - 1]

                if (word1[ri - 1] != word2[ci - 1]):
                    diag += 1
                minT = min(left, top, diag)
                d[ci][ri] = minT

        print(d)

        return d[c][r]