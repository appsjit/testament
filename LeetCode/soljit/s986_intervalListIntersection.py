class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(A)
        n = len(B)

        x, y = 0, 0
        lo, hi = 0, 0

        result = []
        while x < m and y < n:
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection

            lo = max(A[x][0], B[y][0])
            hi = min(A[x][1], B[y][1])

            ## Intersection check
            if lo <= hi:
                result.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[x][1] < B[y][1]:
                x += 1
            else:
                y += 1

        return result


