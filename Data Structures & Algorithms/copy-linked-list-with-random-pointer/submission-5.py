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
        curr = head

        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next

        for node in hmap.keys():
            hmap[node].next = hmap.get(node.next, None)
            hmap[node].random = hmap.get(node.random, None)

        return hmap[head] 
