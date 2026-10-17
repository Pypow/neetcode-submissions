class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # in python heapq.heapify only has minHeap, 
        # we  multiply by -1 to use it as maxheap
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first, second = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            result = abs(first-second)
            if result:
                heapq.heappush(maxHeap, -result)
        heapq.heappush(maxHeap, 0)
        return abs(maxHeap[0])

