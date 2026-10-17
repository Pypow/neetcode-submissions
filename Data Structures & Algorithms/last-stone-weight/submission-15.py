class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            a, b = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            diff = abs(a - b)
            if diff:
                heapq.heappush(maxHeap, -diff)
        return -maxHeap[0] if maxHeap else 0