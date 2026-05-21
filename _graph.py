'''
Graph consist of finite sets of vertices and edges which connects a pair of nodes.
Nodes and Links

Graphs - 
Directed and Undirected
Weighted Unweighted

If a graph is complete or almost complete -> Adjacency Matrix
If number of edges are limited -> Adjacency Matrix

Python Dictionary Implementation:
{
A: []
B: []
C: []
}
'''
class Graph:
    def __init__(self):
        self.adjacency_list={}

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex]=[]
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for other_vertex in list(self.adjacency_list[vertex]):
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])

my_graph=Graph()
print("Vertex")
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.print_graph()

print("\nAdjacency List")
my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")

my_graph.add_edge("B","A")
my_graph.add_edge("B","E")

my_graph.add_edge("C","A")
my_graph.add_edge("C","D")

my_graph.add_edge("D","A")
my_graph.add_edge("D","C")
my_graph.add_edge("D","E")

my_graph.add_edge("E","B")
my_graph.add_edge("E","D")
my_graph.print_graph()

my_graph.remove_vertex("D")
print("\nUpdated List:")
my_graph.print_graph()