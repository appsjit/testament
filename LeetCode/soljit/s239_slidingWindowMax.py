class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) == 0 or len(nums) < k:
            return []

        l, r = 0, k - 1
        res = []
        while l < len(nums) - k + 1:
            res.append(max(nums[l:k + l]))

            l += 1

        return res