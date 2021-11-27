class Solution:
    #     def getMaxLen(self, nums: List[int]) -> int:
    #   Initiate posPrdLen  [0]*L
    #   Initiate negPrdLen  [0]*L
    #               1 -2 -3 4
    # posPrdLen     1  0 3  4
    # negPrdLen     0  2 1  2
    # [1,-2,-3,4]

    #               1 -2 3 4 5 0 1 2 4 6
    # posPrdLen     1  0 1 2 3 0 1 2 3 4
    # negPrdLen     0  2 3 4 5 0 0 0 0 0

    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        # dp[i][0] : max length of subarray ending with index i With positive product
        # dp[i][1] : max length of subarray ending with index i With negative product

        negProductLen = [0] * L  # [[0] for _ in range(L)]
        posProductLen = [0] * L  # [[0] for _ in range(L)]

        if nums[0] > 0:
            posProductLen[0] = 1
        elif nums[0] < 0:
            negProductLen[0] = 1

        res = posProductLen[0]

        for i in range(1, L):

            if nums[i] > 0:
                posProductLen[i] = posProductLen[i - 1] + 1
                if (negProductLen[i - 1] > 0):  # if previous negative subarray exists
                    negProductLen[i] = max(negProductLen[i], negProductLen[i - 1] + 1)

            if nums[i] < 0:
                negProductLen[i] = posProductLen[i - 1] + 1
                if (negProductLen[i - 1] > 0):  # if previous negative subarray exists
                    posProductLen[i] = max(posProductLen[i], negProductLen[i - 1] + 1)

            print('posProductLen[i]:' + str(posProductLen[i]) + '  negProductLen[i]:' + str(negProductLen[i]))
            res = max(res, posProductLen[i])
        return res