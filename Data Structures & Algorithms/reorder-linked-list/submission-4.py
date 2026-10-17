# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, None)

        # get mid node
        slow, fast = head, head     # slow -> mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of LL
        cur = slow
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # Reorder LL
        l, r = head, prev
        tail = dummy
        while l and r and l != r:
            tmpl = l.next
            tmpr = r.next
            tail.next = l
            tail = tail.next
            tail.next = r
            tail = tail.next
            l = tmpl
            r = tmpr





