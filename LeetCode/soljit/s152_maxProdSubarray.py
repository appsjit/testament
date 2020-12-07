class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## Idea is to take care of -ve valies and zero
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        minProduct, maxProduct, resProduct = [nums[0]] * 3

        for i in range(1, len(nums)):
            print('i:' + str(nums[i]) + '  maxProduct:' + str(maxProduct) + '  minProduct:' + str(minProduct))
            if nums[i] >= 0:
                maxProduct = max(nums[i], nums[i] * maxProduct)
                minProduct = min(nums[i], nums[i] * minProduct)
            elif (nums[i] < 0):
                ## Hold max of current and last Min
                ## if zero then max will be zero
                ## if negative then if multiplied with with -ve will be positive
                temp = max(nums[i], nums[i] * minProduct)
                ## For 0 min will be zero
                # For -ve min will multipled by earlier highest value
                minProduct = min(nums[i], nums[i] * maxProduct)
                maxProduct = temp

            resProduct = max(resProduct, maxProduct)
        return resProduct
