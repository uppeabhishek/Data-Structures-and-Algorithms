from collections import deque


class Graph:

    def __init__(self, V, directed=False):
        self.VLength = V
        self.V = [deque() for _ in range(V)]
        self.visited = [False for _ in range(V)]
        self.directed = directed

    def add_edge(self, source, destination):
        self.V[source].append(destination)
        if not self.directed:
            self.V[destination].append(source)

    def isCycleInUndirectedGraphHelper(self, vertex, parent):
        self.visited[vertex] = True
        for c in self.V[vertex]:
            if c != parent and self.visited[c]:
                return True
            if not self.visited[c]:
                if self.isCycleInUndirectedGraphHelper(c, vertex):
                    return True

        return False

    def isCycleInUndirectedGraph(self):
        for i in range(self.VLength):
            if not self.visited[i]:
                if self.isCycleInUndirectedGraphHelper(i, -1):
                    return True
        return False

    def BFSCycleUtil(self, index):
        d = deque()
        d.append(index)

        self.added = [False for _ in range(self.VLength)]

        while d != deque([]):
            top = d.pop()
            self.visited[top] = True
            for neighbour in self.V[top]:
                if not self.visited[neighbour]:
                    if self.added[neighbour]:
                        return True
                    self.added[neighbour] = True
                    d.append(neighbour)
        return False

    def BFSCycle(self):
        for i in range(self.VLength):
            if not self.visited[i]:
                if self.BFSCycleUtil(i):
                    return True
        return False


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(0, 5)
print(g.BFSCycle())
# print(g.isCycleInUndirectedGraph())
