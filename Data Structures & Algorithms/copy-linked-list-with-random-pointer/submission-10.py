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
        # IMP: Handle empty heads
        if not head:
            return None
        hmap = {}   # oldNode: NewNode
        cur = head

        while cur:
            hmap[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        for oldNode in hmap:
            hmap[oldNode].next = hmap[oldNode.next] if oldNode.next else None
            hmap[oldNode].random = hmap[oldNode.random] if oldNode.random else None
            oldNode = oldNode.next
        return hmap[head]
    