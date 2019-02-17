class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        result = list()
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if (nums[i] > 0):
                break

            if (i > 0 and (nums[i] == nums[i - 1])):
                continue
            else:
                mn = i + 1
                mx = len(nums) - 1
                suma = 0 - nums[i]
                while (mn < mx):
                    if (nums[mn] + nums[mx] == suma):
                        print([nums[i], nums[mn], nums[mx]])
                        result.append([nums[i], nums[mn], nums[mx]])

                        while ((mn < mx) and (nums[mn] == nums[mn + 1])):
                            mn = mn + 1
                        while ((mn < mx) and (nums[mx] == nums[mx - 1])):
                            mx = mx - 1
                        mn += 1
                        mx -= 1
                    elif ((nums[mn] + nums[mx]) < suma):
                        mn += 1
                    else:
                        mx -= 1

        return result

