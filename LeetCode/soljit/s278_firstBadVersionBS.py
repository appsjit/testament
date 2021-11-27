# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while (left < right):
            mid = left + (right - left) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return int(left)

        # l, r = 0, n
        #
        # while l <= r:
        #     mid = l + ((r - l) // 2)
        #     if isBadVersion(mid):
        #         if not isBadVersion(mid - 1):
        #             return mid
        #         else:
        #             r = mid
        #     else:
        #         l = mid + 1
        #
        # return -1