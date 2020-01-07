import collections, heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        mdict = collections.defaultdict(int)

        for x in S:
            mdict[x] += 1

        myheap = []

        for k, v in mdict.items():  ## Adding total number of occurences to Dictionary
            heapq.heappush(myheap, (-1 * v, k))

        if (-1 * myheap[0][0] > (len(S) + 1) / 2):
            return ""
        result = ""

        while len(myheap) >= 2:
            tmp = []
            p1, key1 = heapq.heappop(myheap)
            p2, key2 = heapq.heappop(myheap)
            result += key1
            result += key2
            if p1 != -1:
                tmp += [(p1 + 1, key1)]
            if p2 != -1:
                tmp += [(p2 + 1, key2)]

            for rvsdTmp in tmp:
                ##myheap.append(rvsdTmp)
                heapq.heappush(myheap, rvsdTmp)

        print(result)

        return result + (myheap[0][1] if len(myheap) > 0 else '')