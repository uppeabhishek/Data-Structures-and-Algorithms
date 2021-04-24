class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # Stores the last node pointer so adding time complexity will be O(1)
        self.last_node = None


class Graph:
    def __init__(self, V):
        self.V = V
        self.li = [LinkedList() for i in range(V)]

    def add_edge(self, start, end):

        temp = self.li[start].head

        if temp is None:
            self.li[start].head = Node(end)
            self.li[start].last_node = self.li[start].head
        else:
            node = Node(end)
            self.li[start].last_node.next = node
            self.li[start].last_node = self.li[start].last_node.next

    def print_vertices(self):
        for i in range(V):
            temp = self.li[i].head
            print(str(i) + " ->", end=" ")
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print()


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_vertices()
