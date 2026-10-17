# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        while n:
            n -= 1
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        # remove node
        if not fast:
            head = head.next
            return head

        slow.next = slow.next.next
        return head
    