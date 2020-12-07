class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        lp = len(prices)
        profit = [0] * lp

        if lp < 2:
            return 0

        # if k >= len(prices) / 2:
        #     return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        if k >= lp / 2:
            res = 0
            ## a After b before
            ## check in pairs if 2nd day greater then sell and buy
            for a, b in zip(prices[1:], prices[:-1]):
                if (a > b):
                    res += a - b
            return res

        for i in range(k):
            minPrice = prices[0]
            maxPrice = 0

            for j in range(lp):
                minPrice = min(minPrice, prices[j] - profit[j])
                maxPrice = max(maxPrice, prices[j] - minPrice)
                profit[j] = maxPrice

        return profit[lp - 1]

