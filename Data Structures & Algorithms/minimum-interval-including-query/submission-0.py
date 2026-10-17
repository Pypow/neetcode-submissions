class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda i: i[1]-i[0]+1)
        res = []
        flag = False
        for q in queries:
            for inter in intervals:
                flag = False
                if q <= inter[1] and q >= inter[0]:
                    res.append(inter[1]-inter[0]+1)
                    flag = True
                    break
            if not flag:
                flag = False
                res.append(-1)
        return res
