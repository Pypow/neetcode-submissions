class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        newIntervals = []
        res = []
        for s, e in intervals:
            l = e - s + 1
            newIntervals.append([l, s, e])
        newIntervals.sort()
        for q in queries:
            found = False
            for l, s, e in newIntervals:
                if s <= q <= e:
                    found = True
                    res.append(l)
                    break
            if not found:
                res.append(-1)
        return res
