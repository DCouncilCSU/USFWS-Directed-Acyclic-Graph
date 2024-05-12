# USFWS-Directed-Acyclic-Graph
Coding Challenge for US Fish &amp; Wildlife Service, Directed Acyclic Graph implementation in Python with Longest Path function.

## Usage
main.py holds the Graph class and the driver code. The Graph class defines a longestPath function as well as some class and instance variables used by the function. The constructor takes in an adjacency list parameter as shown below:

In the driver code, you must define a valid acyclic graph using an adjacency list:
```
adjacencyList = {
    0 : [1, 2], # node 0 has edges to nodes 1 and 2
    1 : [3, 4], # node 1 has edges to nodes 3 and 4
    2 : [5],    # node 2 has edge to node 5
    3 : [],     # node 3 has no outgoing edges (leaf node)
    4 : [5],    # node 4 has edge to node 5
    5 : []      # node 5 has no outgoing edges (leaf node)
}
```

In the driver code, you can select a starting node, on the line that looks like: 
`graph.getLongestPathFrom(2)`

`2` can be replaced with any valid key from the adjacency graph above

When the program is invoked, an integer of the longest path from the node defined in the driver code will be output, along with some progress indicators

To run the program:
`python main.py`

### How It Works
Since this exercise assumes a Directed Acyclic Graph with equal or no edge weights to be considered, I chose a Depth First Search (DFS) algorithm.

DFS: We start at the chosen node and mark that we have visited this node. We look at the list of adjacent nodes. If there are any, we add 1 to the path length and recurse into the first one we see. This process is repeated until we encounter a node with no adjacent nodes (A leaf). After hitting a leaf, we pop up out of the recursion, and we have gathered a 'depth' that we will use as the path length. If there are other possible paths, we take them and see if they are any longer than the one we just tried. If there are no other possible paths from the starting node, we know we have the longest path.

#### TODOS
* Graph validation in constructor
* Node validation in getLongestPath function

#### Misc
* DFS will provide O(Nodes+Edges) performance
* Graphs with multiple same-length paths will always traverse one or the other