# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy
        while l1 or l2 or carry:
            total = 0
            total += l1.val if l1 else 0
            total += l2.val if l2 else 0
            total += carry
            lastDigit = total % 10
            carry = total // 10
            tail.next = ListNode(lastDigit)
            tail = tail.next
            l1 = l1.next if l1 and l1.next is not None else None
            l2 = l2.next if l2 and l2.next is not None else None
        return dummy.next