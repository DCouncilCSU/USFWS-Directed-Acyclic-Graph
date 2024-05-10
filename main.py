# Directed Acyclic Graph Longest Path Function
# USFWS Coding Challenge
# David Council

# Graph class, does not validate acyclic-ity
class Graph:
    # Declare vertices as a dictionary
    vertices = {}

    # Class Constructor
    def __init__(self, vertices):
        self.vertices = vertices

    # return graph in array sorted such that
    # no element comes before its parent
    def get_topological(self):
        visited = []

        for vertex in self.vertices:
            
    # return integer length of longest path
    def longest_path(self, vertex):
        #iterate through vertices, in topological order
        
            
#MAIN
#{vertex: {set of adjacent edges}, ...}
graph_definition = {0: {1}, 1: {2, 3}, 2: {3}}
graph = Graph(graph_definition)

#print(graph.longest_path(0))
