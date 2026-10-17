class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            a = -heapq.heappop(maxHeap) 
            b = -heapq.heappop(maxHeap)
            diff = abs(a-b)
            if diff:
                heapq.heappush(maxHeap, -diff)
        res = 0
        if maxHeap and abs(maxHeap[0]):
            res = abs(maxHeap[0])
        return res
