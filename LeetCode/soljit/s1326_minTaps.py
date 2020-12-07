class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if n < 1:
            return 0

        intRange = []  ##[0]*(n + 1)

        for i, r in enumerate(ranges):
            ##print(str(max(i-r,0))+"   "+str(min(n,i+r)))
            intRange.append((max(i - r, 0), i + r))
            ##intRange[max(i-r,0)] = min(n,i+r)
        intRange = sorted(intRange)

        print(intRange)

        start, end, tapCnt, i = intRange[0][0], 0, 0, 0
        while i < len(ranges):
            # Below while loop to get maximum end range for one start
            while (i < len(ranges) and intRange[i][0] <= start):
                end = max(end, intRange[i][1])
                i += 1
            print(str(start) + " " + str(end))
            if (end == start):
                return -1
            start = end
            tapCnt += 1
            if start >= n:  ## If reaches till end of garden
                return tapCnt

        return -1






