from CodeSnippets.WeightedGraph import WeightedGraph
from DisjointSet import DisjointSet


class Kruskals:
    def __init__(self, graph, disjoint):
        self.graph = graph
        self.disjoint = disjoint

    def findMinimumSpanningTree(self):
        edges = self.graph.getEdges()
        edges.sort(key=lambda k1: k1[1])

        result = []

        for ele in edges:
            first, second = ord(ele[0][0]) - 65, ord(ele[0][1]) - 65
            if self.disjoint.find(first) == self.disjoint.find(second):
                continue
            self.disjoint.union(first, second)
            result.append(ele[0])

        print(result)


g = WeightedGraph(6, False, True)
g.add_edge('A', ('B', 3))
g.add_edge('A', ('D', 1))
g.add_edge('B', ('D', 3))
g.add_edge('B', ('C', 1))
g.add_edge('C', ('D', 1))
g.add_edge('C', ('E', 5))
g.add_edge('C', ('F', 4))
g.add_edge('D', ('E', 6))
g.add_edge('E', ('F', 2))

d = DisjointSet(6)

k = Kruskals(g, d)
k.findMinimumSpanningTree()
