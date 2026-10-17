class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            dif = abs(heapq.heappop(maxHeap) - heapq.heappop(maxHeap))
            if dif:
                heapq.heappush(maxHeap, -dif)
        return abs(maxHeap[0]) if maxHeap else 0