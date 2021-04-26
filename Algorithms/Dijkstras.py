import heapq
import sys
from collections import defaultdict

from CodeSnippets.WeightedGraph import WeightedGraph


class Dijkstras:
    def __init__(self, graph):
        self.graph = graph

    def findShortest(self, source, destination):

        parent = [None for _ in range(self.graph.getVerticesLength())]
        map_heap = set()

        heap = []
        vertices = self.graph.getVertices()
        distance_dictionary = defaultdict()

        for i in range(self.graph.getVerticesLength()):
            distance_dictionary[i] = sys.maxsize
            map_heap.add(i)

        heapq.heappush(heap, (0, source))
        distance_dictionary[source] = 0
        while heap:
            current_distance, top = heapq.heappop(heap)
            map_heap.discard(top)
            for neighbour, distance in vertices[top]:
                if neighbour in map_heap:
                    previous_distance, new_distance = distance_dictionary[neighbour], current_distance + distance

                    if new_distance < previous_distance:
                        parent[neighbour] = top
                        distance_dictionary[neighbour] = new_distance

                    distance_dictionary[neighbour] = min(distance_dictionary[neighbour], current_distance + distance)
                    heapq.heappush(heap, (current_distance + distance, neighbour))

        result = []
        temp_destination = destination
        while temp_destination != None:
            result.append(temp_destination)
            temp_destination = parent[temp_destination]

        print(f'Shortest Path from {source} to {destination} ==', end=" ")
        while result:
            print(result.pop(), end=" ")
        print()


g = WeightedGraph(6, False)
g.add_edge(0, (1, 5))
g.add_edge(0, (4, 2))
g.add_edge(0, (3, 9))
g.add_edge(1, (2, 2))
g.add_edge(2, (3, 3))
g.add_edge(3, (5, 2))
g.add_edge(4, (5, 3))

d = Dijkstras(g)

for i in range(g.getVerticesLength()):
    for j in range(g.getVerticesLength()):
        d.findShortest(i, j)
