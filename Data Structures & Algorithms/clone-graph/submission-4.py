"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}   # old: new

        def dfs(oldNode):
            if oldNode in hmap:
                return hmap[oldNode]
            newNode = Node(oldNode.val)
            hmap[oldNode] = newNode
            for nei in oldNode.neighbors:
                newNode.neighbors.append(dfs(nei))
            return newNode
        return dfs(node) if node else None
            