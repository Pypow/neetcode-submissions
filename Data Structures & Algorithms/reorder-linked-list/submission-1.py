# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # split the LL in half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second portion of LL
        second = slow.next
        prev = None
        slow.next = None

        while second:
            tempSecond = second.next
            second.next = prev
            prev = second
            second = tempSecond
        
        # merge the two LL
        second = prev
        first = head

        while first and second:
            tempFirst, tempSecond = first.next, second.next
            first.next = second
            second.next = tempFirst
            first, second = tempFirst, tempSecond
        return head




            

        
