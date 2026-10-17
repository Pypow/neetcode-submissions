"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        res = 0 # max meetings
        mr = 0  # current no of meetings
        start = [s.start for s in intervals]
        start.sort()
        end = [e.end for e in intervals]
        end.sort()
        s, e = 0, 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                mr += 1
                s += 1
            else:
                mr -= 1
                e += 1
            res = max(res, mr)
        return res

        

