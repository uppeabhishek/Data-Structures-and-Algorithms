from collections import deque


class WeightedGraph:

    def __init__(self, V, directed=True, isVertexUpperCaseCharacter=False):
        self.VLength = V
        self.V = [deque() for _ in range(V)]
        self.directed = directed
        self.isVertexUpperCaseCharacter = isVertexUpperCaseCharacter

    def getVertices(self):
        return self.V

    def getVerticesLength(self):
        return self.VLength

    def getEdges(self):
        edges = []
        cache = set()
        for i, vertex in enumerate(self.V):
            for v in vertex:
                if self.isVertexUpperCaseCharacter:
                    key = chr(65 + i) + chr(65 + v[0])
                else:
                    key = str(i) + str(v[0])

                if not self.directed:
                    if key[::-1] in cache:
                        continue

                cache.add(key)
                edges.append((key, v[1]))

        return edges

    def add_edge(self, source, destination):
        if isinstance(source, str):
            source = ord(source) - 65

        if isinstance(destination[0], str):
            destination = (ord(destination[0]) - 65, destination[1])

        self.V[source].append(destination)

        if not self.directed:
            self.V[destination[0]].append((source, destination[1]))
