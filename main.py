# Directed Acyclic Graph Longest Path Function
# USFWS Coding Challenge
# David Council

# Graph class, does not validate acyclic-ity
class Graph:
    # Declare graph as a dictionary
    graph = {}
    # Declare List to hold visited vertices
    visitedVertices = []
    # Declare path length starting at 0
    pathLength = 0

    # Class Constructor
    def __init__(self, adjacencyList):
        self.graph = adjacencyList

    def get_longest_path(self, start):
        if start not in self.visitedVertices:
            print("visiting: " + str(start))
            # mark as visited
            self.visitedVertices.append(start)

            # increment path length
            self.pathLength += 1

            # recurse through adjacent vertices
            for adjVertex in self.graph[start]:
                self.get_longest_path(adjVertex)

        # return path length minus one,
        # to account for 0 length at start
        return self.pathLength - 1


# e.g. {vertex: [set of adjacent vertices], ...}
adjacencyList = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [5],
    5: []
}
# construct Graph with adjacency list
graph = Graph(adjacencyList)

print(graph.get_longest_path(1))
