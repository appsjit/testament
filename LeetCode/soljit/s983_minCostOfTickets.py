class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = 366
        dayset = set(days)
        memo = [None]*N

        durations = [1,7,30]
        ## Start with zero and populate the last day first and bring back till first day and compare for one day and seven day passes
        def dp(i):
            if i >= N:
                return 0;

            if memo[i] != None:
                return memo[i]

            ans = float('inf')
            if i in dayset:
                ans = min(dp(i+1)+ costs[0], dp(i+7)+ costs[1], dp(i+30)+ costs[2])
            else:
                ans = dp(i+1)
            ##for c,d in zip(costs, durations):
            memo[i] = ans
            return ans

        return dp(0)
