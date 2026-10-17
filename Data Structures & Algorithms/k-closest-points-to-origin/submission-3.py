class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []  #(distance, point)
        res = []
        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(minHeap, (dist, p))

        while k:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1
        return res
        

