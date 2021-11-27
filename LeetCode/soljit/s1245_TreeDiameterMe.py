class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        myTree = defaultdict(list)
        for u, v in edges:
            myTree[u].append(v)
            myTree[v].append(u)

        maxB = 0
        memo = defaultdict(int)

        def recMaxB(src, pNode, pVal, pTree):
            if (src, pNode) in memo.keys():
                return memo[(src, pNode)]
            edges = [x for x in myTree[pNode] if x != src]
            if len(edges) == 0:
                return pVal
            retVal = 0
            for edge in edges:
                retVal = max(retVal, 1 + recMaxB(pNode, edge, pVal, pTree))
            memo[(src, pNode)] = retVal
            return retVal

        for k, v in myTree.items():
            maxB = max(maxB, recMaxB(None, k, 0, myTree))

        return maxB


