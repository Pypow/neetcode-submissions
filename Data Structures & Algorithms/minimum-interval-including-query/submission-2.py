class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []                # (len(interval[i], r))
        res = {}                    # sorted q: min(len(interval))
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                if q <= intervals[i][1]:
                    l, r = intervals[i][0], intervals[i][1]
                    heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
        