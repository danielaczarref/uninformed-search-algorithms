# Uninformed Search Algorithms - Top 3

## Breadth-first search
Breadth-first search is a simple strategy where the root node is expanded first, then all successors of the root node are expanded, then the successors of those nodes, and so on. In general, all nodes at a given depth in the search tree are expanded before all nodes at the next level are expanded.

![image](https://github.com/danielaczarref/uninformed-search-algorithms/assets/43211679/f6d03aae-e54b-4fe7-b426-e631748efcf3)

Breadth-first search is an instance of the graph-first search algorithm. where the shallowest unexpanded node is chosen for expansion. This is achieved simply by using a FIFO queue for the edge. Thus, new nodes (which are always deeper than their parents) go to the end of the queue, and old nodes, which are shallower than new ones, are expanded first. There is a slight refinement to the generic graph search algorithm, as the objective test is applied to each node when it is generated and not when it is selected for expansion.

## Uniform-cost search 

When all step costs are equal, breadthfirst is optimal because it always expands the shallowest unexpanded node. Through a simple extension, we can find an algorithm that is optimal for any step cost function. Instead of expanding the shallowest node, uniform cost search expands the node n with the lowest g(n) path cost. This is done by storing the edge as a g-ordered priority queue.

The algorithm is identical to the general graph search algorithm, except using a priority queue and adding an extra check if a shortest path to an edge state is discovered.

In addition to the queue order by path cost, there are two other significant differences in breadth-first search. The first is that the objective test is applied to a node when it is selected for expansion (as in the generic graph search algorithm) and not when it is first generated. The reason is that the first objective node that is generated may be on a sub-optimal path. The second difference is that a test is added if a better path is found for a node currently on the edge.

## Depth-first search

Depth-first search always expands to the deepest node on the current edge of the search tree. The search immediately proceeds to the deepest level of the search tree, where the nodes have no successors. As these nodes are expanded, they are pushed away from the edge, and then the search “returns” to the next deeper node that still has unexplored successors.

![image](https://github.com/danielaczarref/uninformed-search-algorithms/assets/43211679/1689c300-824f-419d-b210-da88937139d0)

The depth-first search algorithm is an instance of the graph search algorithm. While breadth-first search uses a FIFO queue, depth-first search uses a LIFO queue. A LIFO queue means that the most recently generated node is chosen for expansion. It should be the deepest unexpanded node because it is deeper than its parent, which in turn was the deepest unexpanded node when it was selected

