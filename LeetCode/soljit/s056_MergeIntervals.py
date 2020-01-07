class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ##print(intervals)
        merged = []
        intervals.sort(key=lambda x: x[0])
        for intx in intervals:

            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < intx[0]:
                merged.append(intx)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                print(merged[-1])
                merged[-1][1] = max(merged[-1][1], intx[1])

        return merged
