class Solution:
    def fib(self, n: int) -> int:
        # n0 = 0 n1 = 1
        if n <= 1:
            return n
        cache = {}
        # def helper(pN):
        #   # Top Down Memoization
        #     if pN <= 1 :
        #         return pN
        #     else :
        #         if pN not in cache:
        #             cache[pN] = helper(pN - 1 ) + helper(pN - 2)
        #         return cache[pN]
        # return helper(n)


        # Bottom Up Tabulation
        cache[0] = 0
        cache[1] = 1
        cache[2] = 1

        for z in range(2, n + 2):
            cache[z] = cache[z - 1] + cache[z - 2] + + cache[z - 3]

        return cache[n]



