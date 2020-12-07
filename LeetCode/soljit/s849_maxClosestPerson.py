import math


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        checkGap = 0
        maxGap = 0
        initGap = 0
        first_man = 0  ##float('inf')
        for i in range(len(seats)):
            if first_man == 0 and seats[i] == 0:
                initGap += 1
            elif first_man > 0 and seats[i] == 0:
                checkGap += 1
            elif seats[i] == 1:
                first_man = i + 1
                maxGap = max(maxGap, checkGap)
                checkGap = 0
        lastGap = 0
        last_man = len(seats)
        for i in range(len(seats) - 1, -1, -1):
            if last_man == len(seats) and seats[i] == 0:
                lastGap += 1
            else:
                break

        res = max(math.ceil(maxGap / 2), initGap, lastGap)

        ##print(res)
        return res
