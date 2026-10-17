class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if end < newInterval[0]:
                res.append([start, end])
            elif newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                tstart = min(start, newInterval[0])
                tend = max(end, newInterval[1])
                newInterval = [tstart, tend]
        # if we exited the loop, then new interval did not overlap at all so we will add it to the end
        res.append(newInterval)
        return res