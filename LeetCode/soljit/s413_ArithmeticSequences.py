class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0

        L = len(nums)

        if (L < 3):
            return 0
        dp = 0
        for x in range(2, L):
            if ((nums[x] - nums[x - 1] == nums[x - 1] - nums[x - 2]) or
                    (nums[x - 1] - nums[x] == nums[x - 2] - nums[x - 1])):
                dp = 1 + dp
                res += dp
            else:
                dp = 0
        return res

