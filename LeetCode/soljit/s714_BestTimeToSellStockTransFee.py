class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #           1   3   2   8   4   9
        # soldMx    0   0   0   5   5   8
        # heldMx    -1  -1  -1  -1  1   1
        L = len(prices)
        sold, held = 0, -prices[0]
        for y in range(1, L):
            presold = sold
            # Max Sold applies fee
            sold = max(presold, held + prices[y] - fee)
            ## Max Hold till previous day
            held = max(held, presold - prices[y])
            print(str(sold) + '   ' + str(held))

        return sold
