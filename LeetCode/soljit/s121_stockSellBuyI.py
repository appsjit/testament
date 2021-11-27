class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if (len(prices)) < 2:
            return 0

        l = float('inf')
        h = 0
        ##print(l < 5)
        curProfit = h - l
        maxProfit = curProfit
        for x in prices:
            l = min(l, x)
            maxProfit = max((x - l), maxProfit)

        return maxProfit

    # class Solution:
    #     def maxProfit(self, prices: List[int]) -> int:
    #         minAmt = float(inf)
    #         res = 0
    #         for x in prices:
    #             minAmt = min(minAmt, x)
    #             res = max(res, x - minAmt)
    #         return res