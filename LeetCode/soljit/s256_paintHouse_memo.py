class Solution:
    ## Pure recursion works for smaller data set. Else Time Limit exceeds
    ## Recursion + Memoization fixes the issue
    def minCost(self, costs: List[List[int]]) -> int:
        lenHouse = len(costs)

        def helper(pidx, prow):
            if (prow, pidx) in self.memo:  ## Added For Memo
                return self.memo[(prow, pidx)]  ## Added For Memo
            if prow >= lenHouse:
                return 0
            totCost = 0
            if (pidx == 0):
                totCost += costs[prow][pidx] + min(helper(1, prow + 1), helper(2, prow + 1))
            if (pidx == 1):
                totCost += costs[prow][pidx] + min(helper(0, prow + 1), helper(2, prow + 1))
            if (pidx == 2):
                totCost += costs[prow][pidx] + min(helper(1, prow + 1), helper(0, prow + 1))
            self.memo[(prow, pidx)] = totCost  ## Added For Memo
            return totCost

        self.memo = {}  ## Added For Memo
        return min(helper(0, 0), helper(1, 0), helper(2, 0))

    ## DP Solution
    # def minCost(self, costs: List[List[int]]) -> int:
    #     lenHouse = len(costs)
    #     dp = costs[:]
    #     if costs == []:
    #         return 0
    #
    #     for revRow in range(lenHouse - 2, -1, -1):
    #         dp[revRow][0] += min(dp[revRow + 1][1], dp[revRow + 1][2])
    #         dp[revRow][1] += min(dp[revRow + 1][0], dp[revRow + 1][2])
    #         dp[revRow][2] += min(dp[revRow + 1][1], dp[revRow + 1][0])
    #
    #     return min(dp[0])
