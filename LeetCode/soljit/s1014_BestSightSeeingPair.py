class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #       0   1   2   3   4
        #       8   1   7   2   9
        #   8   0
        #   1   8   0
        #   7   13  7   0
        #   2   7   1   8   0
        #   9   13  7   14  7   0

        #   P   8   2   9   5
        #   n   0   0   5   -1  5

        #       8   1   5   2   6
        #   P   8   2   7   5   10
        #   n   8   0   3   -1  2

        #   Base Case if i = j

        L = len(values)

        ans = 0
        maxI = values[0]

        for x in range(1, L):
            maxJ = values[x] - x
            ans = max(ans, maxI + maxJ)
            maxI = max(maxI, values[x] + x)

        # Brute Force TimeOut
        # for i in range(L - 1):
        #     for j in range(i, L):
        #         if i < j:
        #             curVal = values[i] + values[j] + i - j
        #             ans = max(ans,  curVal)
        # for i in range(1,L):
        #     print(values[i])

        return ans