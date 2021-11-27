class Solution:
    def dfs(self, pAdjList, pVisited, pNode):
        pVisited.add(pNode)
        for conn in pAdjList[pNode]:
            if conn not in pVisited:
                Solution.dfs(self, pAdjList, pVisited, conn)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        print('test')
        visited = set()
        ans = 0

        ## Create Adjacency List
        adjList = defaultdict(list)
        for frm, to in edges:
            adjList[frm].append(to)
            adjList[to].append(frm)

        ## As mentioned in Solution iterate through nodes
        # When node not in visited then it must be new component
        for x in range(n):
            if x not in visited:
                ans += 1
                Solution.dfs(self, adjList, visited, x)
        print(visited)
        return ans

