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
        hmap = {}       # oldNode: newNode

        cur = head
        while cur:
            hmap[cur] = Node(cur.val)
            cur = cur.next
        
        # Assign references in new LL
        for oldN, newN in hmap.items():
            newN.next = hmap[oldN.next] if oldN.next is not None else None
            newN.random = hmap[oldN.random] if oldN.random is not None else None
        
        return hmap[head]
