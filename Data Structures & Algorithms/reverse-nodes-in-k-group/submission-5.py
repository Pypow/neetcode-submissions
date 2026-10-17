# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        def findKth(node, k):
            while k and node:
                node = node.next
                k -= 1
            return node

        while True:
            kth = findKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next        # IMP: link for unprocessed chain
            # reverse kth group
            cur = groupPrev.next
            prev = kth.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = groupPrev.next        # IMP: link reversed group back to proceed chain
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

