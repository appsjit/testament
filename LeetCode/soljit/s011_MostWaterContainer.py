class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1

        area = min(height[l], height[r]) * (r - l)

        # while (l < r):
        #     chkArea = min(height[l],height[r])*(r-l)
        #     if( chkArea > area):
        #         area = chkArea
        #     if(height[l] < height[r]):
        #         l+=1
        #     else:
        #         r-=1

        while (l < r):
            if (height[l] < height[r]):
                l += 1
                chkArea = min(height[l], height[r]) * (r - l)
                if (chkArea > area):
                    area = chkArea
            else:
                r -= 1
                chkArea = min(height[l], height[r]) * (r - l)
                if (chkArea > area):
                    area = chkArea

        return area
        """
        :type height: List[int]
        :rtype: int
        """
