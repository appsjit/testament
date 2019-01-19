class Solution:
    def twoSum(self, nums, target):
        print(nums)
        numDict = dict()

        result = list()

        for idx in range(len(nums)):
            if ((target - nums[idx]) in numDict.keys()):
                result.append(numDict[target - nums[idx]])
                result.append(idx)
                print(nums[idx])

            numDict[nums[idx]] = idx

        return result

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
