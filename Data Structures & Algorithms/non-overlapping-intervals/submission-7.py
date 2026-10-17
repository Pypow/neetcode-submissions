class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # remove the one that ends last
        # we store the end values of adjacent intervals to detect overlaps
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                res += 1
                prevEnd = min(prevEnd, intervals[i][1])
        return res
        