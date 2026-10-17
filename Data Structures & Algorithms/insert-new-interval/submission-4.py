class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Check if it comes before current interval
        # check if it coms After current interval
        # check if we need to merge with current interval
        res = []
        for i in range(len(intervals)):
            s, e = intervals[i][0], intervals[i][1] 
            # After
            if e < newInterval[0]:
                res.append([s, e])
            # Before
            elif newInterval[1] < s:
                res.append(newInterval)
                return res + intervals[i:]
            # Merge
            else:
                newInterval[0] = min(s, newInterval[0])
                newInterval[1]= max(e, newInterval[1])
        res.append(newInterval)
        return res