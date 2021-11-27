class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stepCost = {}
        L = len(cost)

        # step 0 and step 1 is 0
        stepCost[0] = 0
        stepCost[1] = 0

        # ##### Bottom Up DP Tabulation
        # # Start iteration from step 2, since the minimum cost of reaching
        # for i in range(2, L +1):
        #     firstStep = stepCost[i-1] + cost[i-1]
        #     secondStep = stepCost[i-2] + cost[i-2]
        #     stepCost[i] = min(firstStep, secondStep)
        # # The final element in minimum_cost refers to the top floor
        # return stepCost[L]

        ###  Top Down Recursion + Memoization
        def traverse(pIdx):
            nonlocal stepCost
            if pIdx <= 1:
                return 0

            if pIdx in stepCost:
                return stepCost[pIdx]

            stepOne = cost[pIdx - 1] + traverse(pIdx - 1)
            stepTwo = cost[pIdx - 2] + traverse(pIdx - 2)
            stepCost[pIdx] = min(stepOne, stepTwo)

            return stepCost[pIdx]

        return traverse(L)


