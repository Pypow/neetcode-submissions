# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # IMP: DONT USE DUMMY NODE

        # 1) find middle - IMP : Slow ends at last node of 1st half
        # IMP: slow - head,     fast - head.next
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half
        # Save head of second LL and break the link
        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # inter-twine two lists
        second = prev    # second half
        first = head    # first half
        while first and second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
        

        


