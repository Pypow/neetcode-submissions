# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGrp = dummy

        while True:
            kth = self.getKth(prevGrp, k)
            if not kth:
                break
            nextGrp = kth.next

            # reverse LL
            prev, cur = nextGrp, prevGrp.next
            while cur != nextGrp:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = prevGrp.next
            prevGrp.next = kth
            prevGrp = tmp

        return dummy.next



    def getKth(self, ll, k):
        while ll and k > 0:
            ll = ll.next
            k -= 1
        return ll
        

