class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        prevInterval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if prevInterval[1] < intervals[i][0]:
                res.append(prevInterval)
                prevInterval = intervals[i]
            else:
                prevInterval = [min(prevInterval[0], intervals[i][0]), 
                                max(prevInterval[1], intervals[i][1])]
        res.append(prevInterval)
        return res
