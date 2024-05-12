# Directed Acyclic Graph Longest Path Function
# USFWS Coding Challenge
# David Council

# Graph class, does not validate acyclic-ity
class Graph:
    # Declare graph as a dictionary
    graph = {}

    # Class Constructor
    def __init__(self, adjacencyList):
        self.graph = adjacencyList
        # Declare list to hold visited nodes
        self.visitedNodes = []
        # Declare path length and temp path length starting at 0
        self.pathLength = 0
        self.tempPathLength = 0

    # Function to find longest path from given node
    def getLongestPathFrom(self, start):
        print("Finding longest path from node: " + str(start))
        self.depthFirstSearch(start)
        print("Longest path length: " + str(self.pathLength))

    def depthFirstSearch(self, start):
        if start not in self.visitedNodes:
            print("Visiting node " + str(start))
            # mark as visited
            self.visitedNodes.append(start)

            # if this is not a leaf node
            if len(self.graph[start]):
                # increment temporary path length
                self.tempPathLength += 1
                # recurse through adjacent nodes
                for adjnode in self.graph[start]:
                    self.depthFirstSearch(adjnode)

            # if this is a leaf node
            else:
                # check if it is the longest path so far
                if self.tempPathLength > self.pathLength:
                    self.pathLength = self.tempPathLength
                #reset for next subgraph
                self.tempPathLength = 0

        # return path length
        return self.pathLength

# Driver Code
# e.g. {node: [set of adjacent nodes], ...}
adjacencyList = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [5], 5: []}
# adjacencyList = {0: [1], 1: []}
# adjacencyList = {
#     0: [1, 3], 
#     1: [3, 4], 
#     2: [3, 4, 5], 
#     3: [5], 
#     4: [5], 
#     5: []
# }
# adjacencyList = {
#     0: [1, 3], 
#     1: [2, 4], 
#     2: [3, 4, 5], 
#     3: [4], 
#     4: [5], 
#     5: []
# }

# construct Graph with adjacency list
graph = Graph(adjacencyList)

# print longest path from node 2
graph.getLongestPathFrom(2)
