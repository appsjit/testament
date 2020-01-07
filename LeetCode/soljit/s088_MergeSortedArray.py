class Solution:
    def merge(self, nums1 , m, int, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x, y = 0, 0

        nums1_copy = nums1[:m]
        nums1[:] = []
        while x < m and y < n:

            if nums1_copy[x] < nums2[y]:
                nums1.append(nums1_copy[x])
                x += 1
            else:
                nums1.append(nums2[y])
                y += 1

        if x < m:
            nums1 += nums1_copy[x:]
            ##nums1[x + y:] = nums1_copy[x:]
        if y < n:
            nums1 += nums2[y:]
            ##nums1[x + y:] = nums2[y:]

        return nums1


