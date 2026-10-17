"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hmap = {}
        old = head
        while old:
            newNode = Node(old.val)
            hmap[old] = newNode
            old = old.next
        
        for oldNode in hmap.keys():
            newNode = hmap[oldNode]
            newNode.next = hmap.get(oldNode.next, None)
            newNode.random = hmap.get(oldNode.random, None)
        
        return hmap[head]