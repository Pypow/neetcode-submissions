# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        sortedLis = lists
        while len(sortedLis) > 1:
            mergedLists = []
            for i in range(0, len(sortedLis), 2):
                l1 = sortedLis[i]
                l2 = sortedLis[i + 1] if (i + 1) < len(sortedLis) else None
                mergedLists.append(self.combineLists(l1, l2))
            sortedLis = mergedLists
        return sortedLis[0]
        
    def combineLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next