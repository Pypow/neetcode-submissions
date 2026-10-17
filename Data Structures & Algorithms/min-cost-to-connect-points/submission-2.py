class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build adj
        adj = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        # prim's
        res = 0
        minHeap = [[0, 0]]  # [cost, node] => firstnode
        visit = set()
        while minHeap and len(visit) < len(points):
            c, n = heapq.heappop(minHeap)
            if n in visit:
                continue
            res += c
            visit.add(n)
            for neiCost, nei in adj[n]:
                if nei in visit:
                    continue
                heapq.heappush(minHeap, [neiCost, nei])
        return res

                

