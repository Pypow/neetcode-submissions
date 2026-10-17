class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        # keep the end value that is minimun so that it is less likely to overlap with future intervals
        intervals.sort()
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if prevEnd <= start:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res