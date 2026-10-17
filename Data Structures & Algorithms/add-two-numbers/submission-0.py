# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1
        num2 = l2
        carry = 0
        dummy = ListNode()
        prev = dummy

        while num1 or num2 or carry:
            n1 = num1.val if num1 else 0
            n2 = num2.val if num2 else 0
            num = n1 + n2 + carry
            carry = num // 10
            num = num % 10
            prev.next = ListNode(num)
            prev = prev.next
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
        
        
        return dummy.next




            
