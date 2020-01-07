class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                break

        if first == -1:
            return [first, first]
        for j in range(len(nums) - 1, -1, -1):
            print(j)
            if nums[j] == target:
                last = j
                break

        print(last)
        ##return [max(first - 1,1), min(len(nums) - last + 1, len(nums) - 1)]
        return [first, last]

