class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []    # dist, [x, y]
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, [dist, [x, y]])
        
        while k:
            x, y = heapq.heappop(minHeap)[1]
            res.append([x, y])
            k -= 1
        return res
        
