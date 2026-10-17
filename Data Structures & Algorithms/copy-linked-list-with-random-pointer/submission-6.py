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
        cur = head
        while cur:
            hmap[cur] = Node(cur.val)
            cur = cur.next
        
        # add relationships
        for old_node in hmap.keys():
            hmap[old_node].next = hmap.get(old_node.next, None)
            hmap[old_node].random = hmap.get(old_node.random, None)
        
        return hmap[head]

            
