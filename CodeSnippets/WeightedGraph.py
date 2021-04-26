from collections import deque


class WeightedGraph:

    def __init__(self, V, directed=True):
        self.VLength = V
        self.V = [deque() for _ in range(V)]
        self.directed = directed

    def getVertices(self):
        return self.V

    def getVerticesLength(self):
        return self.VLength

    def add_edge(self, source, destination):
        self.V[source].append(destination)

        if not self.directed:
            self.V[destination[0]].append((source, destination[1]))
