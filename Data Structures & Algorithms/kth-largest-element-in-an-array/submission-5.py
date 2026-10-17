class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap solution: T: O(n + k log(n))    S: O(n)
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, -n)
        while k-1 > 0:
            heapq.heappop(maxHeap)
            k -= 1
        return -maxHeap[0]