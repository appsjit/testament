class Solution:
    def climbStairs(self, n: int) -> int:
        stepCnt = {}

        #         if n == 1:
        #             return 1
        #         stepCnt[1] = 1
        #         stepCnt[2] = 2
        #         if n <= 2:
        #             return stepCnt[n]
        #         for x in range(3, n+1):
        #             stepCnt[x] = stepCnt[x-1]+stepCnt[x-2]

        #         return stepCnt[n]

        def traverse(pIdx):
            nonlocal n
            nonlocal stepCnt

            if pIdx > n:
                return 0
            if pIdx == n:
                return 1;
            if pIdx not in stepCnt:
                stepCnt[pIdx] = traverse(pIdx + 1) + traverse(pIdx + 2)
            return stepCnt[pIdx]

        return traverse(0)