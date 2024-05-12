# Directed Acyclic Graph Longest Path Function
# USFWS Coding Challenge
# David Council


# Graph class, does not validate acyclic-ity
class Graph:
    # Declare graph as a dictionary
    graph = {}
    # Declare list to hold visited vertices
    visitedVertices = []
    # Declare path length starting at 0
    pathLength = 0

    # Class Constructor
    def __init__(self, adjacencyList):
        self.graph = adjacencyList

    def get_longest_path(self, start, tempPathLength):
        if start not in self.visitedVertices:
            print("visiting: " + str(start))
            # mark as visited
            self.visitedVertices.append(start)

            if len(self.graph[start]):
                # increment temporary path length
                tempPathLength += 1
                # recurse through adjacent vertices
                for adjVertex in self.graph[start]:
                    self.get_longest_path(adjVertex, tempPathLength)
            # if this is a leaf node, check if it is the longest path
            else:
                if tempPathLength > self.pathLength:
                    self.pathLength = tempPathLength

        # return path length
        return self.pathLength

# e.g. {vertex: [set of adjacent vertices], ...}
adjacencyList = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [5], 5: []}
# construct Graph with adjacency list
graph = Graph(adjacencyList)

print(graph.get_longest_path(0, 0))
