class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []


def deserialize(n, edges):
    vertices = {}
    while n > 0:
        n -= 1
        vertices[n] = Vertex(n)
    # Vertex(7) -- Vertex(1) total 6
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        vertices[v1].edges.append(vertices[v2])
        vertices[v2].edges.append(vertices[v1])
    # vertices[0] = [1] vertices[1] = [0]
    # UNCOMMENT OUT THIS AREA IF YOU WOULD LIKE TO SEE THE GRAPH YOU'VE BUILT:
    #
    # for vertex_key in vertices:
    #     vertex = vertices[vertex_key]
    #     print('\nID: ' + str(vertex.id))
    #     for edge in vertex.edges:
    #         print('Edge ID: ' + str(edge.id))
    return vertices[0]


graph = deserialize(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])


def findTree(pgraph, n):
    print(pgraph)

    height = [n] * n

    for x in height:
        print(x)


findTree(graph, 6)




