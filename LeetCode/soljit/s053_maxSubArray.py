class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = [nums[0]] * 2

        for i in range(1, len(nums)):
            ## If sum got negative and newer value better
            if (curSum < 0 and curSum < nums[i]):
                curSum = nums[i]
            else:
                curSum = nums[i] + curSum

            maxSum = max(maxSum, curSum)

        return maxSum