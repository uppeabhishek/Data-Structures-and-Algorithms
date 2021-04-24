from collections import deque


class Graph:

    def __init__(self, V, directed=True):
        self.VLength = V
        self.V = [deque() for _ in range(V)]
        self.visited = [False for _ in range(V)]
        self.directed = directed

    def add_edge(self, source, destination):
        self.V[source].append(destination)
        if not self.directed:
            self.V[destination].append(source)

    def DFSHelper(self, index):
        self.visited[index] = True
        for ele in self.V[index]:
            if not self.visited[ele]:
                self.DFSHelper(ele)

    def DFS(self):
        for i in range(self.VLength):
            if not self.visited[i]:
                self.DFSHelper(i)

    def BFS(self):
        queue = deque()
        queue.append(0)

        while queue != deque([]):
            top_ele = queue.popleft()
            if not self.visited[top_ele]:
                print(top_ele)
                self.visited[top_ele] = True
            for neighbour in self.V[top_ele]:
                if not self.visited[neighbour]:
                    print(neighbour)
                    self.visited[neighbour] = True
                    queue.append(neighbour)


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# g.DFS()
# g.BFS()
g.DFSHelper(2)
