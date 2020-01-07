class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x[0])
        for intx in range(len(intervals)):
            if intx > 0:
                if intervals[intx - 1][1] > intervals[intx][0]:
                    return False

        return True