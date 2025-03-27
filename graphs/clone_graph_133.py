# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 
#--------------------------------------------------------------------------------------------------------





"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        # keep dict of visited nodes
        visited = {}

        def dfs(node):
            # depth first search
            if node in visited:
                return visited[node]
            # if node not already visited
            # create copy with value and put in map
            copy = Node(node.val)
            visited[node] = copy
            # for each neighbor of this node (outgoing edge)
            for neighbor in node.neighbors:
                # add neighbors to deep copy and dfs for them 
                copy.neighbors.append(dfs(neighbor))
            # return copied node with neighbors
            return copy
        
        return dfs(node)
    

# EXPLANATION AND COMPLEXITY:
# uses O(V+E) time complexity -- since we use DFS to reconstruct a deep copy of thegraph, we may visit each vertex at most once
# the problem is simple as i realized i could just use depth first search to reconstruct the graph using the provided adjacency list
# simply keep a dict that we can mark vertex/edges as visited and perform dfs on the graph itself