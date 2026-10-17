class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for a, b in points:
            val = a**2 + b**2
            minHeap.append([val, [a, b]])
        heapq.heapify(minHeap)

        res = []
        while k:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1
        
        return res