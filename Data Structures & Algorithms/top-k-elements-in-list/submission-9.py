import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}       # num: count
        minHeap = []    # count: num
        for n in nums:
            if n not in hmap:
                hmap[n] = 0
            hmap[n] += 1
        for key, v in hmap.items():
            heapq.heappush(minHeap, tuple([v, key]))
        while len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while k or minHeap:
            n = heapq.heappop(minHeap)
            res.append(n[1])
            k -= 1
        return res