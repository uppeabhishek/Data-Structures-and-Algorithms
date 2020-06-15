class Graph:
    def __init__(self, V):
        self.V = V;
        self.nodes = [[] for i in range(V)];

    def add_edge(self, start, end):        
        self.nodes[start].append(end);
    
    def print_vertices(self):
        for i in range(self.V):
            print (str(i) + " ->", end=" ")
            for item in self.nodes[i]:
                print (item, end = " ")
            print ()

    def DFSUtil(self, start, visited):
        visited[start] = True;
        print (start, end=" ")
        for ele in self.nodes[start]:
            if not visited[ele]:
                self.DFSUtil(ele, visited);

    def DFS(self, start, visited):
        for i in range(start, self.V):
            if not visited[i]:
                self.DFSUtil(i, visited);
        
        for i in range(0, start):
            if not visited[i]:
                self.DFSUtil(i, visited);



        
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
    
    res = [False]*V;

    graph.print_vertices();

    graph.DFS(2, res);