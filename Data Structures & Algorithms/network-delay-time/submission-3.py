class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm        |       T:O(E * log(V))
        visit = set()
        adj = collections.defaultdict(list)
        
        for u, v, w in times:
            adj[u].append([w, v])
        
        heap = [(0, k)]   # starting, NOT adj[k]
        res = 0

        while heap:
            w1, u1 = heapq.heappop(heap)
            if u1 in visit:             # visit check #1
                continue
            visit.add(u1)
            res = max(res, w1)          
            
            for w2, u2 in adj[u1]:
                if u2 not in visit:     # visit check #2
                    heapq.heappush(heap, (w1 + w2, u2))
        return res if len(visit) == n else -1

