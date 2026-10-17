class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            a, b = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -abs(a-b))
        return -maxHeap[0] if len(maxHeap) == 1 else 0
