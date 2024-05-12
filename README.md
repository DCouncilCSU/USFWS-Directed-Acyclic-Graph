# USFWS-Directed-Acyclic-Graph
Coding Challenge for US Fish &amp; Wildlife Service, Directed Acyclic Graph implementation in Python with Longest Path function.

## Usage
main.py holds the Graph class and the runner code. You must define a valid acyclic graph using an adjacency list:
```
adjacencyList = {
    0 : [1, 2], #node 0 has edges to nodes 1 and 2
    1 : [3, 4], #node 1 has edges to nodes 3 and 4
    2 : [5],    #node 2 has edge to node 5
    3 : [],     #node 3 has no outgoing edges (leaf node)
    4 : [5],    #node 4 has edge to node 5
    5 : []      #node 5 has no outgoing edges (leaf node)
}
```