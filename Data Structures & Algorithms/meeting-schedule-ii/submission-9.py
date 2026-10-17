"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # IMP: Sort both start and end separately
        start = [s.start for s in intervals]
        start.sort()
        end = [e.end for e in intervals]
        end.sort()
        res = 0
        count = 0
        s, e = 0, 0
        while s < len(intervals) and e < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res
            