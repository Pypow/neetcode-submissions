class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # keep track of (size, right value) in minHeap
        # use hashMap to keep track of org pos of queries after sorting
        # tmp sort queries

        # Valid: start val <= q
        # Invalid: end val < q
        intervals.sort()
        hmap = {}
        minHeap = []
        i = 0
        for q in sorted(queries):   # IMP
            
            # add only Valid ones
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, [r - l + 1, r])
                i += 1

            # remove invalid ones
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            hmap[q] = minHeap[0][0] if minHeap else -1
        
        res = [hmap[q] for q in queries]
        return res

