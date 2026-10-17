class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []    # [diff, [x, y]]
        res = []
        for x, y in points:
            diff = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(minHeap, [diff, [x, y]])
        
        while k:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1
        return res
