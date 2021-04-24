from CodeSnippets.Graph import Graph


class TopologicalSort:

    def __init__(self, graph):
        self.graph = graph
        self.visited = [False for _ in range(graph.VLength)]

    def helper(self, index):
        self.visited[index] = True
        for neighbour in self.graph.V[index]:
            if not self.visited[neighbour]:
                self.helper(neighbour)
        self.result.append(index)

    def print(self):
        self.result = []
        for i in range(self.graph.VLength):
            if not self.visited[i]:
                self.helper(i)

        print(self.result[::-1])


g = Graph(8, True)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(4, 7)
g.add_edge(5, 6)
# g.add_edge(5, 2)
# g.add_edge(5, 0)
# g.add_edge(4, 0)
# g.add_edge(4, 1)
# g.add_edge(2, 3)
# g.add_edge(3, 1)

t = TopologicalSort(g)
t.print()
