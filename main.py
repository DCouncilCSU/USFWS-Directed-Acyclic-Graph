# Directed Acyclic Graph Longest Path Function
# USFWS Coding Challenge
# David Council


# Graph class, does not validate acyclic-ity
class Graph:
    # Declare graph as a dictionary
    graph = {}
    # Declare list to hold visited vertices
    visitedVertices = []
    # Declare path length and temp path length starting at 0
    pathLength = 0
    tempPathLength = 0

    # Class Constructor
    def __init__(self, adjacencyList):
        self.graph = adjacencyList

    # Function to find longest path from given node
    def getLongestPath(self, start):
        if start not in self.visitedVertices:
            print("visiting: " + str(start))
            # mark as visited
            self.visitedVertices.append(start)

            # if this is not a leaf node
            if len(self.graph[start]):
                # increment temporary path length
                self.tempPathLength += 1
                # recurse through adjacent vertices
                for adjVertex in self.graph[start]:
                    self.getLongestPath(adjVertex)

            # if this is a leaf node
            else:
                # check if it is the longest path so far
                if self.tempPathLength > self.pathLength:
                    self.pathLength = self.tempPathLength
                #reset for next subgraph
                self.tempPathLength = 0

        # return path length
        return self.pathLength


# e.g. {vertex: [set of adjacent vertices], ...}
# adjacencyList = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [5], 5: []}
adjacencyList = {0: [1, 3], 1: [3, 4], 2: [3, 4, 5], 3: [5], 4: [5], 5: []}
# construct Graph with adjacency list
graph = Graph(adjacencyList)

# print integer of longest path from node 2
print(graph.getLongestPath(0))
