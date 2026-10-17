class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for t in times:
            u, v, w = t
            adj[u].append([w, v])
        
        res = 0
        minH = [[0, k]]
        visit = set()

        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visit:
                continue
            res = max(res, w1)
            visit.add(n1)

            for w2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minH, [w1 + w2, n2])
        return res if len(visit) == n else -1

