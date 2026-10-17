class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-n for n in stones]
        heapq.heapify(minHeap)
        
        while len(minHeap) > 1:
            x, y = abs(heapq.heappop(minHeap)), abs(heapq.heappop(minHeap))
            diff = abs(x - y)
            if diff:
                heapq.heappush(minHeap, -diff)
        return -minHeap[0] if len(minHeap) > 0 else 0
            