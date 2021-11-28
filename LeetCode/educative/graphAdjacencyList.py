from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u,v):
        self.graph[u].append(v)


    def printman(self):
        print(self.graph)


    def readGraph(self):
        for k,v in self.graph.items():
            for conn in v:
                print(str(k)+' -> '+str(conn))

    def BFS(self, cn):

        visited = [False]*len(self.graph)
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(cn)
        visited[cn] = True

        while queue:
            pr = queue.pop(0)
            print(pr, end =" ")
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for child in self.graph[pr]:
                if not visited[child]:
                    visited[child] = True
                    queue.append(child)



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.readGraph()
g.BFS(0)