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

    def DFSCycleUtil(self, index):
        self.visited[index] = True
        self.added[index] = True
        for ele in self.V[index]:
            if not self.visited[ele]:
                if self.DFSCycleUtil(ele):
                    return True
            if self.added[ele]:
                return True

        self.added[index] = False
        return False

    def DFSCycle(self):
        for i in range(self.VLength):
            if not self.visited[i]:
                self.added = [False for _ in range(self.VLength)]
                if self.DFSCycleUtil(i):
                    return True

        return False

    def BFSCycleUtil(self, index):
        d = deque()
        d.append(index)

        while d != deque([]):
            top = d.pop()
            self.visited[top] = True
            for neighbour in self.V[top]:
                if self.visited[neighbour]:
                    return True
                d.append(neighbour)

        return False

    def BFSCycle(self):
        for i in range(self.VLength):
            if not self.visited[i]:
                if self.BFSCycleUtil(i):
                    return True

        return False


g = Graph(6, True)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 5)
g.add_edge(5, 3)
g.add_edge(3, 0)
# result = g.BFSCycle()
# print(result)
print(g.DFSCycle())
