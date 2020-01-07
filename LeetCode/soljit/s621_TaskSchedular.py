import collections, heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ##print(tasks)

        di = collections.defaultdict(int)
        for t in tasks:  ## Dictionary storing occurences of Letter/Task
            di[t] += 1
        ##print(di)

        myheap = []
        for k, v in di.items():  ## Adding total number of occurences to Dictionary
            heapq.heappush(myheap, (-1 * v, k))

        print(myheap)

        cnt = 0

        while myheap:
            tmp = []
            # iterate by min distance between repeating chars
            # e.g. n = 2, then two spaces are needed after A _ _ A
            for coolPeriod in range(n + 1):
                cnt += 1
                if myheap:
                    p, key = heapq.heappop(myheap)
                    print(str(p) + ' ' + key)
                    # only add back to heap if > 1 chars remain
                    if p != -1:
                        tmp += [(p + 1, key)]
                        # if no heap, and no addition to heap, count is complete
                    if not myheap and not tmp:
                        return cnt
            # add back to heap
            for rvsdTmp in tmp:
                heapq.heappush(myheap, rvsdTmp)

        return cnt
