"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # return what is that max no of meeting at any point in time
        if not intervals:
            return 0
        count = res = 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s = e = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


        
