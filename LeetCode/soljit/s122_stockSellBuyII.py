class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = float('inf')

        res = [-1] * len(prices)

        for x in range(len(prices)):
            res[x] = prices[x] - l
            l = prices[x]

        print(res)
        maxProfit = 0
        for y in res:
            if (y > 0):
                maxProfit += y

        return maxProfit
