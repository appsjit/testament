import math
from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        q = PriorityQueue()
        d = lambda t: math.pow(t[0], 2) + math.pow(t[1], 2)
        for x in points:
            q.put((int(d(x)), x))

        print(q)
        res = []

        i = 0
        while i < K:
            res.append(q.get()[1])
            i += 1

        return res