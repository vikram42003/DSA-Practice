# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    # DFS - Time = O(E + V) = O(n) - Space = O(n)

    # We need to create a copy for each node in the graph, and we'll track those copies with a hashap
    # Then, run a dfs with base case node is already in hashmap then just return it from the hashmap
    # otherwise create the node, add it to hashmap and run dfs again recursively for each neighbour
    # and append what it returns to copy's neighbors, and return the copy after going through all neighbors
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        cloneMap = {}

        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]

            copy = Node(node.val)
            cloneMap[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node)
