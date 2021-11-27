class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        myDict = defaultdict(defaultdict)
        #### Build Graph
        for idx, eq in enumerate(equations):
            dividend = equations[idx][0]
            divisor = equations[idx][1]
            myDict[dividend][divisor] = values[idx]
            myDict[divisor][dividend] = 1 / values[idx]

        print(myDict)

        def traverseNodes(pCurNode, pTargetNode, pRes, pVisited):
            pVisited.add(pCurNode)
            retOut = -1.0
            neighbors = myDict[pCurNode]
            if pTargetNode in neighbors:
                retOut = pRes * neighbors[pTargetNode]
            else:
                for nextNeighbor, value in neighbors.items():
                    if nextNeighbor in pVisited:
                        continue
                    retOut = traverseNodes(nextNeighbor, pTargetNode, pRes * value, pVisited)
                    if retOut != -1.0:
                        break
            pVisited.remove(pCurNode)
            return retOut
            ##if

        ans = []
        for dividend, divisor in queries:
            if dividend not in myDict or divisor not in myDict:
                ret = -1.0

            elif dividend == divisor:
                ret = 1.0
            else:
                visited = set()
                ret = traverseNodes(dividend, divisor, 1, visited)

            ans.append(ret)

        return ans
