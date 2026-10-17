class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))   # IMP node1: (cost, node2)
        minHeap = [(0, k)]    # IMP cost, node
        visit = set()
        time = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = max(time, w1)    # IMP don't accumulate cost, use max -> at given time, we can send msg to all neighbours simultaneously
            for w2, n2 in adj[n1]:
                if n2 not in visit: # IMP
                    heapq.heappush(minHeap, (w2 + w1, n2))
        return time if len(visit) == n else -1


            