class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in  range(1, n+1)}
        for u, v, t in times:
            adj[u].append([t, v])
        minH = [[0, k]]
        visit = set()
        res = 0
        while minH:
            t1, i = heapq.heappop(minH)
            if i in visit:
                continue
            res = max(res, t1)
            visit.add(i)

            for t2, j in adj[i]:
                if j not in visit:
                    heapq.heappush(minH, [t2 + t1, j])
        return res if len(visit) == n else -1