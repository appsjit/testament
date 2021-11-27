class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7
        matrixPair = list(zip(speed, efficiency))

        ## Sort by descending efficiency
        matrixSorted = sorted(matrixPair, key=lambda x: x[1], reverse=True)

        # Use minHeap to maintain speed
        q = []
        calcSum, maxPerf = 0, 0

        for sp, eff in matrixSorted:
            ## heap of k members and take of lowest speed out
            if (len(q) > k - 1):
                calcSum -= heapq.heappop(q)

            heapq.heappush(q, sp)
            calcSum += sp
            maxPerf = max(maxPerf, calcSum * eff)

        return maxPerf % modulo


