# // package whatever; // don't place package name!
#
# Dynamic Programming - Minimum Coin Change
# Prompt:
# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make
# up that amount. If that amount of money cannot be made up by any combination of
# the coins, return -1.
#
# Examples:
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.

class cnCh:
    def coinChange(pcoins, pamt):
        res = [pamt]*(pamt+1)
        print(res)
        res[0] = 0
        for x in range(1,pamt+1):
            for c in range(len(coins)):
                remAmt = x - coins[c]
                if (remAmt >= 0):
                    res[x] = min(res[x], 1 + res[remAmt])

        if(res[pamt] == pamt +1  ):
            return -1
        return res[pamt]

        ##        pass ##print(coins[c])

coins = [1, 2, 5]
amount = 11
print(cnCh.coinChange(coins, amount))
print(cnCh.coinChange([2], 3))
