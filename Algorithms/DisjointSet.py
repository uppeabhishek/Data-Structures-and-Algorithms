class DisjointSet:
    def __init__(self, vertices):
        self.rank = [0] * vertices
        self.parent = [i for i in range(vertices)]

    def find(self, i):
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i, j = self.find(i), self.find(j)

        if i == j:
            return

        if self.rank[i] == self.rank[j]:
            self.parent[j] = i
            self.rank[i] += 1
        elif self.rank[i] < self.rank[j]:
            self.parent[i] = j
        else:
            self.parent[i] = j

    def print(self):
        print(self.parent)
        print(self.rank)


d = DisjointSet(2)
d.union(0, 1)
d.union(1, 0)
